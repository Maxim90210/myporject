from motor.motor_asyncio import AsyncIOMotorClient

class MongoDB:
    def __init__(self, uri):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client['url_shortener']

    def get_collection(self, name):
        return self.db[name]

mongodb = MongoDB('mongodb://mongo:27017')
