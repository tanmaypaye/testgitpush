import pymongo
client = pymongo.MongoClient("mongodb+srv://Tanmay:Password@tanmay.si14ffa.mongodb.net/?retryWrites=true&w=majority")
db = client.test
databese = client['page5']
collections = databese['page5.1']
data = {'h1': 'a', 'h2': 'b', 'h3': 'c'}




