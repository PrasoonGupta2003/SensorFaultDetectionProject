import os


AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = os.getenv("DATABASE_NAME")
MONGO_COLLECTION_NAME = os.getenv("COLLECTION_NAME")


TARGET_COLUMN = "quality"
MONGO_DB_URL = os.getenv("MONGODB_URL")


MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"