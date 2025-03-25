import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["mycollection"]

#sort ascending
for x in mycol.find().sort("name",1): #1:ascending or by default
  print(x)