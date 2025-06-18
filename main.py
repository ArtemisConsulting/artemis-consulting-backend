from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # from frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
try:
    client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017"))
    db = client.artemis_db
    print("Connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

@app.get("/")
async def root():
    return {"message": "Artemis Consulting API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 