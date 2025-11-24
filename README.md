# 🧠 Mental Health Chatbot  
### AI-Powered Emotional Support & NLP-Based Conversation Assistant

A fully functional Mental Health Chatbot built using **FastAPI**, **NLP**, and a lightweight rule-based emotional response engine.  
This chatbot helps users by detecting emotions, analyzing sentiment, and generating supportive, empathetic responses.

This project demonstrates **NLP**, **API development**, **testing**, **frontend integration**, and **DevOps** practices — suitable for product-based companies, AI roles, and backend positions.

---

## 🌟 Features

- 💬 Context-aware chatbot  
- 🧠 Emotion Detection (stress, anxiety, sadness, anger, happiness, neutral)  
- 😊 Sentiment Classification (positive, neutral, negative)  
- 🔄 Multi-turn conversation support  
- ✨ Preprocessing utilities  
- ⚙️ FastAPI backend with /predict endpoint  
- 🌐 Simple HTML Chat UI  
- 🧪 Unit tests using pytest  
- 🐳 Docker + docker-compose support  
- 🔁 CI/CD workflow using GitHub Actions  
- 📘 Clean project structure with docs, tests, and models folders  

---

## 🧱 Architecture Overview

```
User  
  ↓  
Chat UI (HTML/JS)  
  ↓  
FastAPI Backend (/predict API)  
  ↓  
NLP Engine  
  ↓  
Emotion + Sentiment Classifier  
  ↓  
Empathetic Response Generator  
  ↓  
Reply to User  
```

---

## 📁 Project Structure

```
mental_health_chatbot/
│
├── src/
│   ├── api/
│   │   └── app.py                # FastAPI app
│   ├── nlp/
│   │   └── predict.py            # Emotion + Sentiment logic
│   └── utils/
│       └── preprocess.py         # Preprocessing helpers
│
├── models/                       # Model files placeholder
├── data/                         # Dataset placeholder
├── tests/
│   └── test_api.py               # Unit tests
│
├── frontend/
│   └── index.html                # Simple UI
│
├── docs/
│   └── architecture.md           # Documentation
│
├── requirements.txt              # Dependencies
├── Dockerfile                    # Build container
├── docker-compose.yml            # Run container
├── .github/workflows/ci.yml      # GitHub Actions CI
└── README.md
```

---

## ⚙️ Technology Stack

- **Backend:** FastAPI (Python)  
- **NLP:** Custom rule-based emotion engine  
- **Frontend:** HTML + JavaScript  
- **Testing:** pytest  
- **DevOps:** Docker, Docker Compose, GitHub Actions  

---

## ▶️ Running the Project Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Start Backend Server
```bash
uvicorn src.api.app:app --reload --port 8000
```

### 3️⃣ Access Chat UI  
Open your browser and go to:  
```
http://localhost:8000
```

---

## 📥 API Usage

### **POST /predict**

Request:
```json
{
  "message": "I feel stressed and lonely."
}
```

Response:
```json
{
  "emotion": "stress",
  "sentiment": "negative",
  "reply": "I’m sorry you're feeling stressed. I'm here with you."
}
```

---

## 🧪 Testing

Run the test suite:
```bash
pytest
```

---

## 🐳 Docker Support

### Build:
```bash
docker build -t mental_chatbot .
```

### Run:
```bash
docker-compose up
```

---

## 🚀 CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/ci.yml`) includes:
- Dependency installation  
- Automated testing  
- Linting (optional)  

---

## 📌 Why This Project Is Valuable

This project showcases your abilities in:

- NLP  
- Backend Development  
- Microservices Structure  
- API Design  
- Testing  
- DevOps & CI/CD  
- Documentation  

Perfect for:
- Salesforce  
- Amazon  
- Microsoft  
- Any product-based company or AI startup  

---


