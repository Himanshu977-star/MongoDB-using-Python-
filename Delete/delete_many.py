import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["mycollection"]

#delete many
x=mycol.delete_many({}) #it is not iterable
print(x.deleted_count,"documents deleted.")