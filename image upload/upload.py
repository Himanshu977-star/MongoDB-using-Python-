import pymongo
import gridfs

myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["images"]

fs=gridfs.GridFS(mydb) #divide imaage into smaller chunk of 255kb each and store

#upload image
with open(r'MongoDB using Python\image upload\sample.png', 'rb') as file:
  image_id=fs.put(file,filename='sample.png')

print(f"Image uploaded with id: {image_id}")  