import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["mycollection"]

#advance query
myquery={"$regex":"^S"}
for x in mycol.find({"name":myquery},{"_id":0}):
  print(x)