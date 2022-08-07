import pymongo
client = pymongo.MongoClient("mongodb+srv://Tanmay:Password@tanmay.si14ffa.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['myinfo']
collection = database['tan10']

# record = collection.find()
# for i in record:
#     print(i)

# data = collection.find({'sub': 'data science'})
# for i in data :
#     print(i)

data = collection.find({'batteryVoltageStableTime': {'$gt': 0}})
for i in data:
    print(i)


