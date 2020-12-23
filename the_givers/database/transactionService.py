from models import Transactions
import sys
from app import db
from utils import testData
import json
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

# Add a transaction to the db
def addTransaction(sender_id, receiver_id, amount):
    newTransaction = Transactions(
        sender_id=sender_id, receiver_id=receiver_id, amount=amount
    )
    try:
        db.session.add(newTransaction)
        db.session.commit()
        return 1
    except IntegrityError as e:
        print(e.__dict__)
        if isinstance(e.orig, UniqueViolation):
            return "Transaction associated with that amount and time already exists"
    return "Could not process transaction"

# Get all transactions to a specific organization from the db
def getTransactionsByOrg(receiver_id):
    result = Transactions.query.filter_by(receiver_id=receiver_id)
    if result == None:
        return "No transactions associated with this charity"
    transformedTrans = []
    for transaction in result:
        transformedTran = Transactions(
            sender_id=transaction.sender_id,
            receiver_id=transaction.receiver_id,
            amount=transaction.amount,
            time=transaction.time,
        ).__repr__()
        transformedTrans.append(transformedTran)
    return transformedTrans
