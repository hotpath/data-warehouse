from random import randrange

from pymongo import MongoClient


# * densities row col visits floor minute

def generate():
    mongo = MongoClient('mongodb://localhost:27017')
    db = mongo.cein

    for d in range(1000):
        db.densities.insert_one({
            "floor": randrange(0, 2),
            "row": randrange(0, 2384),
            "col": randrange(0, 1684),
            "visits": randrange(2, 50),
            "minute": randrange(0, 60)
        })

generate()
