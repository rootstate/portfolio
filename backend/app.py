from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis, os
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="My Portfolio API",
    description="A showcase", 
    version="1.0.0"
)

class StatusModel(BaseModel):
    name: str
    desc: str 
    time: str 

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
@app.get("/status", response_model=StatusModel)
def backend_status_message():
    dt = datetime.now()

    return StatusModel(
        name="Portfolio API",
        desc="API is running successfully on port 8000", 
        time=dt.isoformat()
    )

# An api counter endpoint
@app.get("/api/counter")
def counter():
    total = redis_client.incr("page visits")
    return {"visits": total}
