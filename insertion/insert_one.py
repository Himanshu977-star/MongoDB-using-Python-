import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["mycollection"]

#insert one
mydict = { "name": "John", "address": "Highway 37" }
x=mycol.insert_one(mydict)
print(x)
print(x.inserted_id)