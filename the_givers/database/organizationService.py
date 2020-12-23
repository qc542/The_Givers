from models import Organizations
import sys
from app import db
from utils import testData
import json

# Add an organization to the db
def addOrganization(name, email, location=None, category=None, summary=None):
    newOrg = Organizations(
        name=name, email=email, location=location, category=category, summary=summary
    )
    try:
        db.session.add(newOrg)
        db.session.commit()
        return 1
    except IntegrityError as e:
        print(e.__dict__)
        if isinstance(e.orig, UniqueViolation):
            return "Account associated with that email already exists"
    return "Could not register account"


def getOrganizationById(id):
    result = Organizations.query.filter_by(org_id=id).first()
    if result == None:
        return "Organization not found"
    org = result.__repr__()
    newName = org["name"].replace(" ", "-")
    org["name"] = newName
    imageId = testData.imageIdByCharityName[newName]
    org["imageId"] = imageId
    org["news"] = testData.newsByCharityName[newName]
    org["imageName"] = str(imageId) + ".png"
    return org

# Get a specific organization from the db
def getOrganizationByName(name):
    result = Organizations.query.filter_by(name=name).first()
    if result == None:
        return "Organization not found"
    org = result.__repr__()
    newName = org["name"].replace(" ", "-")
    org["name"] = newName
    imageId = testData.imageIdByCharityName[newName]
    org["imageId"] = imageId
    org["news"] = testData.newsByCharityName[newName]
    org["imageName"] = str(imageId) + ".png"
    return org


def getAllCharities():
    result = Organizations.query.all()
    if result == None:
        return "No organizations found"
    transformedOrgs = []
    for org in result:
        newName = org.name.replace(" ", "-")
        if newName == "testName":
            continue
        transformedOrg = Organizations(
            name=newName,
            email=org.email,
            location=org.location,
            category=org.category,
            summary=org.summary,
        ).__repr__()
        imageId = testData.imageIdByCharityName[newName]
        transformedOrg["imageId"] = imageId
        transformedOrg["news"] = testData.newsByCharityName[newName]
        transformedOrg["imageName"] = str(imageId) + ".png"
        transformedOrgs.append(transformedOrg)
    return transformedOrgs
