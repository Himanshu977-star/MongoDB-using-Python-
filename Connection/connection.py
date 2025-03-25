import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]

dblist=myclient.list_database_names()
if "mydatabases" in dblist:
  print("The database exists.")
else:
  print("The database does not exist.")  