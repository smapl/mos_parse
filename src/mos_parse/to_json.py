import json
from pymongo import MongoClient

db = MongoClient()
collection = db["news"]
documents = collection.find({})

data = [doc for doc in documents]
with open("news.json", "a") as file_data:
    json.dump(data, file_data)
