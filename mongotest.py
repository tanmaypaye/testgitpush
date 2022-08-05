import pymongo
client = pymongo.MongoClient("mongodb+srv://Tanmay:Password@tanmay.si14ffa.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    'name':'tanmay',
    'mail':'tanmaypaye@gmail.com',
    'surname':'paye'
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)