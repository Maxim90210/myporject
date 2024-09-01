from .mongodb import mongodb

class URLStorage:
    def __init__(self):
        self.collection = mongodb.get_collection('urls')

    async def save_url(self, short_id, original_url):
        document = {
            'short_id': short_id,
            'original_url': original_url,
            'clicks': 0
        }
        await self.collection.insert_one(document)

    async def get_url(self, short_id):
        document = await self.collection.find_one({'short_id': short_id})
        return document

    async def increment_clicks(self, short_id):
        await self.collection.update_one({'short_id': short_id}, {'$inc': {'clicks': 1}})
