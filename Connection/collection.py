import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]

mycol=mydb["mycollection"]

collist=mydb.list_collection_names()
if "mycollection" in collist:
  print("The collection exists.")
else:
  print("The collection does not exist.")