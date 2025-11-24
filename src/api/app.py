from fastapi import FastAPI
from pydantic import BaseModel
from src.nlp.predict import analyze_message

app = FastAPI(title="Mental Health Chatbot")

class Message(BaseModel):
    message: str

@app.post("/predict")
def predict(msg: Message):
    result = analyze_message(msg.message)
    return result

@app.get("/")
def home():
    return {"status": " Mental Health Chatbot is running "}
