from fastapi import HTTPException
from deepgram import Deepgram
from deepgram.models import Transcription, Model
from typing import Dict, Any
import os
import requests

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

if not DEEPGRAM_API_KEY:
    raise Exception("DEEPGRAM_API_KEY environment variable is not set")

deepgram = Deepgram(DEEPGRAM_API_KEY)

async def generate_speech(text: str, model_id: str) -> str:
    """
    Generates speech from text using the Deepgram API.

    Args:
        text (str): The text to be converted to speech.
        model_id (str): The ID of the Deepgram voice model to use.

    Returns:
        str: The URL of the generated audio file.

    Raises:
        HTTPException: If the Deepgram API request fails or returns an error.
    """
    try:
        response: Dict[str, Any] = deepgram.speech.synthesize(
            text=text,
            model=Model(model_id),
            voice=Model(model_id),
            format="mp3",
        )
        return response["url"]
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Deepgram API request failed: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating speech: {e}")