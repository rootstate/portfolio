from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import redis, os

app = FastAPI()

# Create client
redis = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"), 
    port=6379,
    decode_responses=True
)

# Must change in prod
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# API status checker
@app.get("/status")
def backendStatusMessage():
    return {"status": "OK"}

# An api counter endpoint
@app.get("/api/counter")
def counter():
    total = redis.incr("page visits") # Use of redis integer key that automatically increments
    return {"visits": total}


