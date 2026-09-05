import json
import os
from motor.motor_asyncio import AsyncIOMotorClient
from config import DB_URI, DB_NAME

class Database:
    def __init__(self, uri, database_name):
        self._client = AsyncIOMotorClient(uri)
        self.db = self._client[database_name]

db = Database(DB_URI, DB_NAME)

class Database:
    def __init__(self, data_file="anime_list.json"):
        self.data_file = data_file

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"anime": []}

    def save_data(self, data):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_anime(self, anime_name: str):
        data = self.load_data()
        data["anime"].append(anime_name)
        self.save_data(data)

    def get_anime_list(self):
        data = self.load_data()
        return data.get("anime", [])

db = Database()
