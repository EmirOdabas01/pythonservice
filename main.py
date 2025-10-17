from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gradio_client import Client

# FastAPI uygulaması
app = FastAPI(title="HuggingFace Sentiment API")

# Request model
class PredictRequest(BaseModel):
    text: str

# Hugging Face Client (private space ise token ekle)
hf_client = Client("emir1415/chat-sentiment-ai")  # private ise: Client("emir1415/chat-sentiment-ai", hf_token="YOUR_TOKEN")

# POST endpoint
@app.post("/predict")
async def predict(request: PredictRequest):
    try:
        result = hf_client.predict(
            text=request.text,
            api_name="/predict"
        )
        return {"sentiment": result}  # örn: "Positive"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
