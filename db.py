
import pymongo
from bson.json_util import dumps


class Mongo:
    USERNAME = "kopyl"
    PASSWORD = "oleg66"
    IP = "0.0.0.0"


client = pymongo.MongoClient(
    f"mongodb://"
    f"{Mongo.USERNAME}:{Mongo.PASSWORD}@"
    f"{Mongo.IP}"
)

db = client["users_render_com"]
users_collection = db["users"]


def get_users():  # [ { "username": "freski" } ]
    users = users_collection.find()
    users = list(users)
    users = [
	    {i: x for (i, x) in u.items() if i != "_id"}
	    for u in users
	]
    return users
