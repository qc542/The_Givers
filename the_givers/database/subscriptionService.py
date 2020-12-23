from models import Subscriptions
from app import db
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

# Get subscriptions for given userId
def getSubscriptions(userId):
    entries = Subscriptions.query.filter_by(user_id=userId)
    if entries == None:
        print("No Entries found for user: ", userId)
        return []
    transformedEntries = []
    for entry in entries:
        transformedEntries.append(entry.__repr__())
    return transformedEntries


def isSubscribed(userId, orgId):
    entries = Subscriptions.query.filter_by(user_id=userId, org_id=orgId).first()
    if entries == None:
        return False
    return True
    #


# add to subscription table
def addSubscription(userId, orgId):
    newEntry = Subscriptions(user_id=userId, org_id=orgId)
    try:
        db.session.add(newEntry)
        db.session.commit()
        return 1
    except IntegrityError as e:
        print(e.__dict__)
        if isinstance(e.orig, UniqueViolation):
            return "Subscription already exists"
    return "Did not create subscription"


# remove from subscription table
def removeSubscription(userId, orgId):
    entry = Subscriptions.query.filter_by(user_id=userId, org_id=orgId).first()
    try:
        db.session.delete(entry)
        db.session.commit()
        return 1
    except Exception as e:
        return e.__str__()
    return "Did not remove subscription"
