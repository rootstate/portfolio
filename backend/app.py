from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis, os

app = FastAPI(
    title="My Portfolio API",
    description="A showcase of backend development skills", 
    version="1.0.0"
)

# Create client
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"), 
    port=6379,
    decode_responses=True
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API status checker
@app.get("/status")
def backend_status_message():
    return {"status": "OK"}

# An api counter endpoint
@app.get("/api/counter")
def counter():
    total = redis_client.incr("page visits")
    return {"visits": total}
