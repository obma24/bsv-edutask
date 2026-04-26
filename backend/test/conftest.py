import os

import pymongo
import pytest


@pytest.fixture
def mongo_client():
    mongo_url = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
    try:
        client = pymongo.MongoClient(mongo_url, serverSelectionTimeoutMS=1500)
        client.admin.command("ping")
        return client
    except Exception:
        pytest.skip("MongoDB is not reachable (set MONGO_URL or start MongoDB)")


@pytest.fixture
def it_collection_name():
    return "todo_it"


@pytest.fixture
def clean_it_collection(mongo_client, it_collection_name):
    db = mongo_client.edutask
    if it_collection_name in db.list_collection_names():
        db.drop_collection(it_collection_name)
    yield it_collection_name
    if it_collection_name in db.list_collection_names():
        db.drop_collection(it_collection_name)
