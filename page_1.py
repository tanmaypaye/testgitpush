import pymongo
client = pymongo.MongoClient("mongodb+srv://Tanmay:Password@tanmay.si14ffa.mongodb.net/?retryWrites=true&w=majority")
mydb = client.test

data01 = {'l': 'q', 'k': 'w', 'j': 'e', 'h': 'r'},{'g': 't', 'f': 'y', 'd': 'u', 's':'i'}

database  = client['prv']
collections = database['prv.1']


# data01 = collections.find()