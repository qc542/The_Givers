from database import transactionService
import uuid

testTransactions = []
years = ['2019-01-04', '2019-02-04', '2019-03-04', '2019-04-04', '2019-05-04', '2019-06-04', '2019-07-04', '2019-08-04', '2019-09-04', '2019-10-04', '2019-11-04', '2019-12-04', 
            '2020-01-04', '2020-02-04', '2020-03-04', '2020-04-04', '2020-05-04', '2020-06-04', '2020-07-04', '2020-08-04', '2020-09-04', '2020-10-04', '2020-11-04', '2020-12-04',
            '2020-12-04'
    ]
donations = [25, 15, 30, 45, 10, 15, 30, 15, 25, 15, 45, 55, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 60]
for i in range(len(years)):
    testTransactions.append(
        {
            "sender_id": "d21b44c9-0f2b-496a-9ff1-7f6155fb25aa",
            "reciever_id": "516fe247-a6eb-4712-9531-887d83ffcc6a",
            "amount": donations[i],
        }
    )

for transaction in testTransactions:
    result = transactionService.addTransaction(
        transaction["sender_id"], transaction["reciever_id"], transaction["amount"]
    )
    print(result)