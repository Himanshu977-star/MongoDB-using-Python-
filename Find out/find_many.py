import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["mycollection"]

#find many
name=input("Enter the name:")
for x in mycol.find({"name":name},{"_id":0}): #0:not show, 1:show
 print(x)