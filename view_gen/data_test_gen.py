from random import randrange

from pymongo import MongoClient


# * densities row col visits floor minute

def generate():
    mongo = MongoClient('mongodb://localhost:27017')
    db = mongo.cein

    for d in range(4000):
        db.densities.insert_one({
            "floor": randrange(0, 3),
            "row": randrange(379, 1605),
            "col": randrange(582, 1271),
            "visits": randrange(70, 1000),
            "minute": randrange(0, 60)
        })

generate()
