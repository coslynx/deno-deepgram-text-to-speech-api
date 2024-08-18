from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import schemas
import services.speech_service as speech_service
import utils.auth as auth
import utils.rate_limiter as rate_limiter
import database

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.engine.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.engine.dispose()

# Dependency injection for database sessions
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Authentication middleware
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")
    if token:
        try:
            user = auth.get_current_user(token=token.split(" ")[1])
            request.state.user = user
        except HTTPException:
            raise HTTPException(status_code=401, detail="Invalid token")
    return await call_next(request)

# Rate limiting middleware
@app.middleware("http")
async def rate_limiter_middleware(request: Request, call_next):
    user = request.state.user if hasattr(request.state, 'user') else None
    if user:
        try:
            await rate_limiter.rate_limiter(user=user)
        except HTTPException:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
    return await call_next(request)

@app.post("/speech", response_model=schemas.SpeechResponse)
async def generate_speech(
    request: Request,
    text: str,
    model_id: str,
    db: Session = Depends(get_db),
):
    user = request.state.user if hasattr(request.state, 'user') else None
    if user:
        audio_url = await speech_service.generate_speech(text=text, model_id=model_id)
        return {"audio_url": audio_url}
    else:
        raise HTTPException(status_code=401, detail="Authentication required")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)