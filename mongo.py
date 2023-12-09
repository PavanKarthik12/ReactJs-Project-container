from pymongo import MongoClient

# Replace the following variables with your MongoDB connection details
mongo_uri = "mongodb+srv://pvarada72:5qTEyl4dGOMByxS0@cluster0.bm3zxvc.mongodb.net/?retryWrites=true&w=majority"
# Create a MongoClient
client = MongoClient(mongo_uri)

print(client)
"""
# Access the database (replace 'your_database_name' with your actual database name)
db = client.your_database_name

# Now you can work with your MongoDB database
# For example, you can access a collection and fetch documents
collection = db.your_collection_name
documents = collection.find()

for document in documents:
    print(document)
"""

# Close the connection when done
client.close()
