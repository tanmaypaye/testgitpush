import pymongo
client = pymongo.MongoClient("mongodb+srv://Tanmay:Password@tanmay.si14ffa.mongodb.net/?retryWrites=true&w=majority")
mydb = client.test

data01 = [{'l': 'q', 'k': 'w', 'j': 'e', 'h': 'r'}, {'g': 't', 'f': 'y', 'd': 'u', 's':'i'}]

database  = client['prv']
collection = database['prv.11R']
# collection.insert_one(data01)
# collection.insert_many(data01)
# collection.update_one({'l': 'q'}, {'$set': {'l': 'z'}})
# collection.delete_one({'l': 'z'})
collection.delete_one({'g':'t'})
d = collection.find({'g' :'t'})
# collection.find()
for i in d:
    print(i)