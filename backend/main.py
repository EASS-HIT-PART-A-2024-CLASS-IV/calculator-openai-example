from fastapi import FastAPI, HTTPException
import redis
import json

from pydantic import BaseModel

class Req(BaseModel):
    a: int
    b: int

my_app = FastAPI()

# Initialize Redis client
r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)


@my_app.post("/add")
async def add_numbers(req: Req):
    a = req.a
    b = req.b
    result = a + b
    try:
        # Log the request and result in Redis
        request_id = r.incr("request_id")
        r.set(f"request:{request_id}", json.dumps({"a": a, "b": b, "result": result}))
    except redis.RedisError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"result": result}
