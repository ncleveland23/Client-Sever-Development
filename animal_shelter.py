from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:45314' % (username, password))
        # where xxxxx is your port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            if data:
                self.database.animals.insert(data)  # data should be dictionary            
                return True
        else:
            raise Exception("Nothing to save, because data parameter is empty!")
            return False

# Create method to implement the R in CRUD. 
    def read(self, search):
        if search is not None:
            # if search:
                searchResults = self.database.animals.find(search, {"_id": False})
                return searchResults
        else:
            exception("Nothing to search, becuase search parameter is empty!")
            return exception

# Create method to implement the U in CRUD.
    def update(self, search, updateData):
        if search is not None:
            if search:
                updateResults = self.database.animals.update_many(search, updateData)
                return updateResults
        else:
            exception("Nothing to update, because update parameter is empty!")
            return exception
            
# Create method to implement the D in CRUD.
    def delete(self, search):
        if search is not None:
            if search:
                deleteResults = self.database.animals.delete_many(search)
                return deleteResults
        else:
            exception("Nothing to delete, because delete parameter is empty!")
            return exception