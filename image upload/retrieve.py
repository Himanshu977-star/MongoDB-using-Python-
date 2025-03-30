import pymongo
import gridfs
from bson import ObjectId

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["images"]

# Initialize GridFS
fs = gridfs.GridFS(mydb)

# Retrieve image
image_id = input("Enter Image ID: ")  # Get the image ID from user

image_data = fs.get(ObjectId(image_id))  # Retrieve the image from GridFS

# Save the image to a file
with open(r'MongoDB using Python\image upload\downloaded.png', 'wb') as file:
    file.write(image_data.read())  # Write the retrieved image data to the file

print("Image Downloaded Successfully!")
