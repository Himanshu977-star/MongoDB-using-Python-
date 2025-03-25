import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["mycollection"]

#advance query
myquery={"name":{"$gt":"B"}}#greater than or equal to B and $lt for less than
for x in mycol.find(myquery):
  print(x)