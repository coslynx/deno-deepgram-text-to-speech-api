import pytest
import requests
from services.speech_service import generate_speech
from deepgram import Deepgram
from deepgram.models import Model

DEEPGRAM_API_KEY = "your_deepgram_api_key"  # Replace with your actual Deepgram API key

deepgram = Deepgram(DEEPGRAM_API_KEY)

@pytest.mark.asyncio
async def test_generate_speech_success():
    text = "This is a test."
    model_id = "deepgram_model_id"  # Replace with a valid Deepgram voice model ID
    audio_url = await generate_speech(text, model_id)
    assert audio_url.startswith("https://")

@pytest.mark.asyncio
async def test_generate_speech_invalid_model_id():
    text = "This is a test."
    model_id = "invalid_model_id"
    with pytest.raises(requests.exceptions.RequestException):
        await generate_speech(text, model_id)

@pytest.mark.asyncio
async def test_generate_speech_empty_text():
    text = ""
    model_id = "deepgram_model_id"
    with pytest.raises(requests.exceptions.RequestException):
        await generate_speech(text, model_id)

@pytest.mark.asyncio
async def test_generate_speech_deepgram_error():
    text = "This is a test."
    model_id = "deepgram_model_id"
    deepgram.speech.synthesize = lambda **kwargs: {"url": None}  # Mock Deepgram error
    with pytest.raises(requests.exceptions.RequestException):
        await generate_speech(text, model_id)