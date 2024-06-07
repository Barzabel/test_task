from pymongo import MongoClient


class MongoDB(object):
    def __init__(self, host: str = 'localhost',
                 port: int = 27017,
                 db_name: str = 'db_test',
                 collection: str = 'collection_name_test'):
        self._client = MongoClient(f'mongodb://{host}:{port}')
        self._collection = self._client[db_name][collection]


    def get_data(self, gte, lte):

        data = self._collection.find({"dt": { 
            '$gte': gte,
            '$lte': lte,
        }})
        return [value for value in data]

