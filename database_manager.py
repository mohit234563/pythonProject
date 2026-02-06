import pymongo
from pymongo import MongoClient

class DatabaseManager:
    def __init__(self):
        # Replace with your actual MongoDB Atlas connection string
        self.uri = "mongodb+srv://<password>@cluster0.dp50xs7.mongodb.net/"
        self.client = MongoClient(self.uri)
        self.db = self.client['LabQuizDB']
        self.collection = self.db['Subjects']

    def get_all_subjects(self):
        return self.collection.distinct("subject_name")

    def get_subject_data(self, subject_name):
        return self.collection.find_one({"subject_name": subject_name})