# Simple demo NLP logic (replace with ML model if needed)

import random

emotions=["stress","anxiety","sadness","anger","neutral","happy"]
sentiments=["positive","neutral","negative"]

def analyze_message(text: str):
    # Demo placeholders – randomly assign emotion
    emotion=random.choice(emotions)
    sentiment=random.choice(sentiments)

    reply_map={
        "stress": "I’m sorry you're feeling stressed. I'm here with you.",
        "anxiety":"It's okay to feel anxious. Let's take a slow deep breath.",
        "sadness":"I'm sorry you're feeling low. Want to talk more about it?",
        "anger":"It's natural to feel angry sometimes. I'm listening.",
        "neutral":"I'm here to listen. Tell me more.",
        "happy":"That's great to hear! Keep sharing your thoughts."
    }

    return {
        "emotion": emotion,
        "sentiment": sentiment,
        "reply": reply_map.get(emotion,"I'm here for you.")
    }
