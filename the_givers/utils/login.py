#!/usr/bin/python

from hashlib import sha512
from sqlite3 import connect

f = "data/database.db"


def login(user, password):
    db = connect(f)
    c = db.cursor()
    query = "SELECT * FROM users WHERE user=?"
    sel = c.execute(query, (user,))

    # records with this username
    # so should be at most one record (in theory)

    for record in sel:
        password = sha512(password.encode("utf-8")).hexdigest()
        if password == record[1]:
            return ""  # no error message because it will be rerouted to mainpage
        else:
            return "Invalid password"  # error message
    db.close()

    return "User does not exist"  # error message


def register(user, password):
    db = connect(f)
    c = db.cursor()
    try:  # does table already exist?
        c.execute("SELECT * FROM users")
    except:  # if not, this is the first user!
        c.execute("CREATE TABLE users (user TEXT, password TEXT)")
    db.commit()
    db.close()
    return insert_user(user, password)  # register helper


def insert_user(user, password):  # register helper
    db = connect(f)
    c = db.cursor()
    reg = check_user(user, password)
    if reg == "":  # if error message is blank then theres no problem, update database
        query = "INSERT INTO users VALUES (?, ?)"
        password = sha512(password.encode("utf-8")).hexdigest()
        c.execute(query, (user, password))
        db.commit()
        db.close()
        return 1
    db.commit()
    db.close()
    return reg  # return error message


def check_user(user, password):  # error message generator
    if check_duplicate(user):  # checks if username already exists
        return "Username already exists"
    if " " in user:
        return "Spaces not allowed in username"
    return ""


def check_duplicate(user):  # checks if username already exists
    db = connect(f)
    c = db.cursor()
    query = "SELECT * FROM users WHERE user=?"
    sel = c.execute(query, (user,))
    retVal = False
    for record in sel:
        retVal = True
    db.commit()
    db.close()
    return retVal
