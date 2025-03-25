import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["mycollection"]

#delete one
x=mycol.delete_one({ "address": "Mountain 21" })
print(x.deleted_count,"documents deleted.")