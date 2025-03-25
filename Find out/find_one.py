import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["mycollection"]

#find one
name=input("Enter the name:")
x=mycol.find_one({"name":name},{"_id":0})
print(x)