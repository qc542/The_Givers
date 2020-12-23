from models import Users
import sys
from app import db
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from hashlib import sha512


def login(email, password):
    result = Users.query.filter_by(email=email).first()
    if result == None:
        return "User does not exist"
    user = result.__repr__()
    hashedPassword = sha512(password.encode("utf-8")).hexdigest()
    if hashedPassword == user["password"]:
        return ""
    return "Invalid password"


def register(email, password):
    hashedPassword = sha512(password.encode("utf-8")).hexdigest()
    newUser = Users(email=email, password=hashedPassword)
    try:
        db.session.add(newUser)
        db.session.commit()
        return 1
    except IntegrityError as e:
        print(e.__dict__)
        if isinstance(e.orig, UniqueViolation):
            return "Account associated with that email already exists"
    return "Could not register account"


def getUserIdByEmail(email):
    result = Users.query.filter_by(email=email).first()
    if result == None:
        return "User not found"
    return result.__repr__()
