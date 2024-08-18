from fastapi import HTTPException
import aioredis
import upstash
import os
from typing import Optional
from models.user import User

UPSTASH_REDIS_URL = os.getenv("UPSTASH_REDIS_URL")
if not UPSTASH_REDIS_URL:
    raise Exception("UPSTASH_REDIS_URL environment variable is not set")

redis = aioredis.from_url(UPSTASH_REDIS_URL)

async def rate_limiter(user: User):
    """
    Enforces rate limiting based on user's usage limit.
    """
    key = f"rate_limit:{user.id}"
    remaining_requests = await redis.get(key)
    if remaining_requests is None:
        remaining_requests = user.usage_limit
        await redis.set(key, remaining_requests, ex=3600)  # 1 hour expiration
    
    if int(remaining_requests) <= 0:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    await redis.decr(key)