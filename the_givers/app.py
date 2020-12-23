from flask import Flask, flash, render_template, request, session, url_for, redirect
import sqlite3
import os
import json
import urllib
from newsapi.newsapi_client import NewsApiClient
from flask_sqlalchemy import SQLAlchemy
from utils import testData
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd

import uuid

# Define Application
app = Flask(__name__)
app.debug = True
app.secret_key = "  \x43\xd2\x34\x92\x5b\x4a\x80\xfc\xc6\xb0\x0e\x45\xdd\x51\x36\xc0\xd2\x3a\x85\x42\x57\xbb\x61\xf2\x7b\xb6\xfc\x17\x3b\x1a\xda\x5b\x6d\x7d\x0a\xff\xd3\x6f\xfa\x7c\x1b\xa8\x0f\x7f\x53\x18\x8d\x91\x16\x81"

# Define DB
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:Straussclassof2021!@thegiversdb.cv0g22qfy3ep.us-east-1.rds.amazonaws.com/postgres"
app.config["SQLALCHEMY_ECHO"] = True
app.config["DEBUG"] = True
db = SQLAlchemy(app)

# import is here to avoid circular import errors due to db
from database import (
    userService,
    organizationService,
    transactionService,
    subscriptionService,
    newsfeedService,
)

# Define the ReusableForm class
class ReusableForm(Form):
    status = TextField("Status:", validators=[validators.required()])


# helper function that would be in utils but here for now for testing / demo purposes
def get_news(charity_name):
    all_articles = NewsApiClient(
        api_key="6223800a4d1b497597b28a33cd56e043"
        # api_key="54c63a9d4bad47bf97a59c8764581008" backup
    ).get_everything(q='"' + charity_name + '"')["articles"]
    results = list()
    for article in all_articles:
        results.append([article["title"], article["description"]])
    return results


# helper function to format data for plotting
def format_data(
    x, y, format_func, x_label="Date", y_label="Donation", plot_type="line"
):
    df = format_func(pd.DataFrame({x_label: x, y_label: y}))

    if plot_type == "bar":
        data = [go.Bar(x=df[x_label], y=df[y_label])]
    elif plot_type == "pie":
        data = [go.Pie(x=df[x_label], y=df[y_label])]
    else:
        data = [go.Scatter(x=df[x_label], y=df[y_label])]

    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


def group_by_time(df, type):
    if type == "year":
        return df.groupby(df["Date"].dt.year).mean().reset_index()
    elif type == "month":
        dfM = df[df["Date"].dt.year == 2020]
        dfM = dfM.groupby(dfM["Date"].dt.month).mean().reset_index()
        dfM["Date"] = dfM["Date"].map(
            {
                1: "Jan",
                2: "Feb",
                3: "Mar",
                4: "Apr",
                5: "May",
                6: "Jun",
                7: "Jul",
                8: "Aug",
                9: "Sep",
                10: "Oct",
                11: "Nov",
                12: "Dec",
            }
        )
        return dfM

def filter(charities, currentFilters, filterArg, filterType):
    if filterArg in currentFilters[filterType]:
        currentFilters[filterType].remove(filterArg)
    else:
        currentFilters[filterType].append(filterArg)

    result = [
        charity["name"]
        for charity in charities
        if charity[filterType] in currentFilters[filterType]
    ]
    
    return currentFilters, result

# Define Routes (Controller-ish)
@app.route("/")
def homepage():
    # If user logged in, get charities that he is subscribed to and all charitites for search.
    charities = organizationService.getAllCharities()
    print(charities)
    if "Email" in session:
        userId = userService.getUserIdByEmail(session.get("Email"))["user_id"]
        subscriptions = subscriptionService.getSubscriptions(userId)

        if len(subscriptions) == 0:
            return render_template("home.html", charities=charities)

        subNames = []
        for subEntry in subscriptions:
            org = organizationService.getOrganizationById(subEntry["org_id"])
            subNames.append(org["name"])

        session["subscriptions"] = subNames
        return render_template("home.html", charities=charities, email=session["Email"])
    else:
        error = request.args.get("error")
        success = request.args.get("success")
        return render_template(
            "home.html", charities=charities, success=success, error=error
        )


@app.route("/filter/home/", methods=["POST"])
def filter_home():
    data = request.get_json()
    filterArg = data.get("filter")
    filterType = data.get("type")
    charities = organizationService.getAllCharities()

    if session.get("filters") == None:
        session["filters"] = {"category": [], "location": []}

    currentFilters, result = filter(charities, session["filters"], filterArg, filterType)

    session["filters"] = currentFilters
    session["filteredCharities"] = result
    return render_template(
        "home.html",
        charities=charities,
        filters=currentFilters,
    )
    
@app.route("/filter/search/<query>", methods=["POST"])
def filter_search(query):
    data = request.get_json()
    filterArg = data.get("filter")
    filterType = data.get("type")
    charities = [ charity for charity in organizationService.getAllCharities() if query in charity['name'].replace("-", " ").lower() ]
    print(charities)

    if session.get("filters") == None:
        session["filters"] = {"category": [], "location": []}

    currentFilters, result = filter(charities, session["filters"], filterArg, filterType)

    session["filters"] = currentFilters
    session["filteredCharities"] = result
    print(result)
    return render_template(
        "search.html",
        charities=charities,
        filters=currentFilters,
        query=query
    )


@app.route("/authenticate/", methods=["POST"])
def authenticate():
    pw = request.form["pass"]
    em = request.form["email"]
    tp = request.form["action"]  # login vs. register

    if tp == "login":
        text = userService.login(em, pw)
        if text == "":  # if no error message, succesful go back home
            session["Email"] = em
            return redirect(url_for("homepage", success="You have logged in"))
        return redirect(url_for("homepage", error=text))
    elif tp == "register":
        return redirect("/register")


@app.route("/register/")
def register():
    error = request.args.get("error")
    return render_template("register.html", error=error)


@app.route("/create/account", methods=["POST"])
def create_account():
    em = request.form["email"]
    pw1 = request.form["pass1"]
    pw2 = request.form["pass2"]
    print(request.form["user_type"])
    if pw1 != pw2:
        return redirect(url_for("register", error="Passwords don't match!"))
    # insert data to database
    if request.form["user_type"] == "manager":
        return redirect(url_for("register_charity"))
    return redirect(url_for("homepage", success="You have registered"))


@app.route("/register/charity")
def register_charity():
    return render_template("create_charity.html")


@app.route("/create/charity", methods=["POST"])
def create_charity():
    print(request.form)
    #  return redirect(url_for("create_charity", error="Some Error"))
    return redirect(url_for("homepage", success="You have registered"))


@app.route("/logout/")
def logout():
    session.pop("Email")
    return redirect(url_for("homepage", success="You have successfully logged out"))


@app.route("/search/")
def search():
    query = request.args.get("search").lower()
    print(query)

    charities = [ charity for charity in organizationService.getAllCharities() if query in charity['name'].replace("-", " ").lower() ]
    print(charities)
    if "Email" in session:
        userId = userService.getUserIdByEmail(session.get("Email"))["user_id"]
        subscriptions = subscriptionService.getSubscriptions(userId)

        if len(subscriptions) == 0:
            return render_template("search.html", charities=charities, query=query)

        subNames = []
        for subEntry in subscriptions:
            org = organizationService.getOrganizationById(subEntry["org_id"])
            subNames.append(org["name"])

        session["subscriptions"] = subNames
        return render_template("search.html", charities=charities, email=session["Email"], query=query)
    else:
        error = request.args.get("error")
        success = request.args.get("success")
        return render_template(
            "search.html", charities=charities, success=success, error=error, query=query
        )


@app.route("/profile")
def profilePage():
    firstName = userService.getUserIdByEmail(session.get("Email"))["name"]
    
    years = [
        "2019-01-04",
        "2019-02-04",
        "2019-03-04",
        "2019-04-04",
        "2019-05-04",
        "2019-06-04",
        "2019-07-04",
        "2019-08-04",
        "2019-09-04",
        "2019-10-04",
        "2019-11-04",
        "2019-12-04",
        "2020-01-04",
        "2020-02-04",
        "2020-03-04",
        "2020-04-04",
        "2020-05-04",
        "2020-06-04",
        "2020-07-04",
        "2020-08-04",
        "2020-09-04",
        "2020-10-04",
        "2020-11-04",
        "2020-12-04",
        "2020-12-04",
    ]

    donations = [
        25,
        15,
        30,
        45,
        10,
        15,
        30,
        15,
        25,
        15,
        45,
        55,
        10,
        20,
        30,
        40,
        50,
        60,
        70,
        80,
        90,
        100,
        110,
        120,
        60,
    ]

    yearly_donations = format_data(
        pd.DatetimeIndex(years), donations, lambda df: group_by_time(df, type="year")
    )
    monthly_donations = format_data(
        pd.DatetimeIndex(years), donations, lambda df: group_by_time(df, type="month")
    )

    return render_template(
        "profile.html",
        firstName=firstName,
        yearly_donations=yearly_donations,
        monthly_donations=monthly_donations,
    )


@app.route("/testPage")
def testPage():
    # charities = testData.populatedCharities
    # for i in range(len(charities)):
    #     charities[i][3].extend(get_news(charities[i][1]))
    return render_template("testPage.html", Email="test@gmail.com")


@app.route("/charity/<name>")
def charityHome(name):
    session["charityName"] = name
    orgInfo = organizationService.getOrganizationByName(name.replace("-", " "))
    session["charityLogo"] = orgInfo["imageName"]

    followState = "Follow"
    # If user is logged in
    if session.get("Email"):
        userId = userService.getUserIdByEmail(session["Email"])["user_id"]
        orgId = organizationService.getOrganizationByName(name.replace("-", " ")).get(
            "org_id"
        )
        # if no errors getting ids and the subscription entry exists...
        print(userId, orgId)
        newsfeedPosts = newsfeedService.getNewsfeedPosts(orgId)
        if (
            type(userId) != str
            and type(orgId) != str
            and subscriptionService.isSubscribed(userId, orgId)
        ):
            followState = "Unfollow"
    else:
        # TODO get org_id of organization and query for newsfeed posts for that org_id
        newsfeedPosts = newsfeedService.getNewsfeedPosts(
            "c17a594a-d3f8-4a46-ae59-da368c67c05d"
        )
        # The org_id above belongs to the Red Cross
        # If the user is not logged in, display posts from the Red Cross by default

    return render_template(
        "charityHomePage.html",
        name=name,
        location=orgInfo["location"],
        description=orgInfo["summary"],
        subOffset=0,
        followUnfollow=followState,
        newsfeedPosts=newsfeedPosts,
    )


@app.route("/post_status", methods=["GET", "POST"])
def post_status():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == "POST":
        status = request.form["status"]

    if form.validate():
        newsfeedService.addNewsfeedPost(
            "Status Update", status, None, None, "c17a594a-d3f8-4a46-ae59-da368c67c05d"
        )
        # The org_id belongs to the Red Cross
        flash("Your message is now on the news feed.")
    else:
        flash("Error: no text was entered.")

    return render_template("post_status.html", form=form)


@app.route("/create/order", methods=["POST"])
def create_order():
    am = request.form["amount"]
    name = session["charityName"]
    if name == "":
        return redirect(
            url_for("charityHome"), error="There was an error connecting to the charity"
        )
    if int(am) < 0.99:
        return redirect(
            url_for(
                "charityHome", name=name, error="The amount entered is less than $1"
            )
        )
    return redirect(url_for("checkout", amount=am, name=name))


@app.route("/checkout")
def checkout():
    name = request.args.get("name")
    amount = request.args.get("amount")
    imageName = session["charityLogo"]

    return render_template(
        "checkout.html", amount=amount, name=name, imageName=imageName
    )


@app.route("/subscription/<kind>", methods=["POST"])
def toggleFollow(kind):
    data = request.get_json()
    userEm = data.get("userEm")
    orgName = data.get("orgName")

    org = organizationService.getOrganizationByName(orgName)
    if type(org) == str:
        print(org)
        return org
    orgId = org.get("org_id")

    userId = userService.getUserIdByEmail(userEm)["user_id"]
    if type(userId) == str:
        print(userId)
        return userId

    if kind == "Follow":
        success = subscriptionService.addSubscription(userId, orgId)
        if success != 1:
            print(success)
            return success
        if orgName not in session["subscriptions"]:
            session["subscriptions"].append(orgName)
        return "sucessfully followed"
    elif kind == "Unfollow":
        success = subscriptionService.removeSubscription(userId, orgId)
        if success != 1:
            print(success)
            return success
        if orgName in session["subscriptions"]:
            session["subscriptions"].remove(orgName)
        return "sucessfully unfollowed"
    else:
        print("there was an error in the request")
        return "Error, could not understand request"


@app.route("/profile/<name>/analytics", methods=["GET"])
def showTables(name):
    session["charityName"] = name
    orgInfo = organizationService.getOrganizationByName(name.replace("-", " "))
    print(orgInfo, type(orgInfo))
    res = transactionService.getTransactionsByOrg(
        "c17a594a-d3f8-4a46-ae59-da368c67c05d"
    )
    years = []
    donations = []
    for i in res:
        years.append(i["time"])
        donations.append(i["amount"])
    df = pd.DataFrame({'Date': pd.DatetimeIndex(years), 'Donation': donations})
    dfY = df.groupby(df['Date'].dt.year).mean().reset_index()
    dfM = df[df['Date'].dt.year == pd.datetime.now().year]
    dfM = dfM.groupby(dfM['Date'].dt.month).mean().reset_index()
    dfM['Date'] = dfM['Date'].map({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'})

    dataY = [go.Scatter(x=dfY["Date"], y=dfY["Donation"])]
    dataM = [go.Scatter(x=dfM["Date"], y=dfM["Donation"])]

    yJSON = json.dumps(dataY, cls=plotly.utils.PlotlyJSONEncoder)
    mJSON = json.dumps(dataM, cls=plotly.utils.PlotlyJSONEncoder)

    sectors = ["Never Donated", "Donated Once", "Donated At Least Once"]
    subscribers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    # refers to how many times each subscriber has donated
    donCount = [0, 3, 1, 1, 2, 0, 0, 1, 5, 1]
    # update values for easier organization
    donCount2 = [2 if x > 1 else x for x in donCount]
    donCount2 = [donCount2.count(0), donCount2.count(1), donCount2.count(2)]

    donData = [go.Pie(labels=sectors, values=donCount2)]
    donJSON = json.dumps(donData, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("analytics.html", graph1=yJSON, graph2=mJSON, graph3=donJSON)


if __name__ == "__main__":
    app.run()
