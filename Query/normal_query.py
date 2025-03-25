import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["mycollection"]

#normal query
name=input("Enter the name:")
myquery={"name":name}

for x in mycol.find(myquery):
  print(x)