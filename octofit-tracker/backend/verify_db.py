import pymongo
import json

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']

def check_collection(collection_name):
    """Check if a collection exists and has data."""
    collection = db[collection_name]
    count = collection.count_documents({})
    print(f"{collection_name} count: {count}")
    
    if count > 0:
        print("Sample document:")
        print(json.dumps(collection.find_one(), default=str, indent=2))
    print("-" * 50)

print("Database verification")
print("=" * 50)

# Check collections
collections = ["auth_user", "octofit_tracker_user", "octofit_tracker_team", 
               "octofit_tracker_activity", "octofit_tracker_leaderboard", 
               "octofit_tracker_workout"]

for collection in collections:
    check_collection(collection)

# List all collections in the database
print("All collections in the database:")
collections = db.list_collection_names()
print(collections)
