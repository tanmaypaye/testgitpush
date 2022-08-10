import pymongo
client = pymongo.MongoClient("mongodb+srv://Tanmay:Password@tanmay.si14ffa.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['page4']
collections = database['4.1']
data = {'q': 1, 'w': 2, 'e':3, 'r': 4, 5: 'm', 6: 'n', 7: 'b'}