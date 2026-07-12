from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import pandas as pd
import json
import os
import certifi

# Load environment variables
load_dotenv()

# Read values from .env
uri = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

print(uri)

# Connect to MongoDB
client = MongoClient(
    uri,
    tls=True,
    tlsCAFile=certifi.where()
)

# Read dataset
df = pd.read_csv(
    r"C:\Users\prave\OneDrive\Desktop\Coding\DataScience\MachineLearning\SensorFaultDetectionProject\notebooks\wafer_23012020_041211.csv"
)

# Drop unnecessary column
df = df.drop("Unnamed: 0", axis=1)

# Convert DataFrame to JSON records
json_record = list(json.loads(df.T.to_json()).values())

# Insert into MongoDB
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

print("Data uploaded successfully!")