from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import services.speech_service as speech_service
from database import get_db

router = APIRouter(
    prefix="/speech",
    tags=["speech"],
    responses={404: {"description": "Speech generation failed"}},
)

@router.post("/", response_model=schemas.SpeechResponse)
async def generate_speech(
    text: str,
    model_id: str,
    db: Session = Depends(get_db),
):
    user = None
    if hasattr(db.state, 'user'):
        user = db.state.user
    if user:
        audio_url = await speech_service.generate_speech(text=text, model_id=model_id)
        return {"audio_url": audio_url}
    else:
        raise HTTPException(status_code=401, detail="Authentication required")