from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import ARRAY, JSON
from app import db
from uuid import uuid4
import datetime


class Financials(db.Model):
    __tablename__ = "financials"
    __table_args__ = {"schema": "public"}

    external_id = db.Column(db.Integer)
    financial_id = db.Column(
        "financial_id",
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        default=uuid4,
        primary_key=True,
    )

    def __repr__(self):
        return {external_id: self.external_id, financial_id: self.financial_id}


class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = {"schema": "public"}

    user_id = db.Column(
        UUID(as_uuid=True), unique=True, nullable=False, default=uuid4, primary_key=True
    )
    name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    financial_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Financials.financial_id))
    managed_org_id = db.Column(ARRAY(UUID(as_uuid=True)))

    def __repr__(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "financial_id": self.financial_id,
            "managed_org_id": self.managed_org_id,
        }

class Organizations(db.Model):
    __tablename__ = "organizations"
    __table_args__ = {"schema": "public"}

    org_id = db.Column(
        UUID(as_uuid=True), unique=True, nullable=False, default=uuid4, primary_key=True
    )
    name = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    financial_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Financials.financial_id))
    location = db.Column(db.Text)
    category = db.Column(db.Text)
    summary = db.Column(db.Text)

    def __repr__(self):
        return {
            "org_id": self.org_id,
            "name": self.name,
            "email": self.email,
            "financial_id": self.financial_id,
            "location": self.location,
            "category": self.category,
            "summary": self.summary,
        }

class Transactions(db.Model):
    __tablename__ = "transactions"
    __table_args__ = {"schema": "public"}

    transaction_id = db.Column(
        UUID(as_uuid=True), unique=True, nullable=False, default=uuid4, primary_key=True
    )
    sender_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("users.user_id"), unique=True, nullable=False
    )
    receiver_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("organizations.org_id"),
        unique=True,
        nullable=False,
    )
    amount = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())

    def __repr__(self):
        return {
            "transaction_id": self.transaction_id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "amount": self.amount,
            "time": self.time,
        }


class Subscriptions(db.Model):
    __tablename__ = "subscriptions"
    __table_args__ = {"schema": "public"}

    user_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey(Users.user_id),
        unique=True,
        nullable=False,
        primary_key=True,
    )
    org_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey(Organizations.org_id),
        unique=True,
        nullable=False,
    )

    def __repr__(self):
        return {"user_id": self.user_id, "org_id": self.org_id}


class Goals(db.Model):
    __tablename__ = "goals"
    __table_args__ = {"schema": "public"}

    goal_id = db.Column(
        UUID(as_uuid=True), unique=True, nullable=False, default=uuid4, primary_key=True
    )
    org_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("organizations.org_id"), nullable=False
    )
    start_time = db.Column(
        db.DateTime(timezone=True), default=datetime.datetime.now(), nullable=False
    )
    end_time = db.Column(db.DateTime(timezone=True))
    expected_amount = db.Column(db.Integer, nullable=False)
    transaction_ids = db.Column(ARRAY(UUID(as_uuid=True)))

    def __repr__(self):
        return {
            goal_id: self.goal_id,
            org_id: self.org_id,
            start_time: self.start_time,
            end_time: self.end_time,
            expected_amount: self.expected_amount,
            transaction_ids: self.transaction_ids,
        }


class NewsFeedPost(db.Model):
    __tablename__ = "newsfeedposts"
    __table_args__ = {"schema": "public"}

    post_id = db.Column(
        UUID(as_uuid=True), unique=True, nullable=False, default=uuid4, primary_key=True
    )
    title = db.Column(db.Text, unique=True, nullable=False)
    body = db.Column(db.Text, unique=True)
    api_params = db.Column(ARRAY(JSON))
    api_links = db.Column(ARRAY(db.Text))
    time = db.Column(
        db.DateTime(timezone=True), default=datetime.datetime.now(), nullable=False
    )
    org_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey(Organizations.org_id), nullable=False
    )

    def __repr__(self):
        return {
            "post_id": self.post_id,
            "title": self.title,
            "body": self.body,
            "api_params": self.api_params,
            "api_links": self.api_links,
            "time": self.time,
            "org_id": self.org_id,
        }
