from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

def get_reply(user_text):
    t = user_text.lower().strip()

    # Explicit language/offensive/rude
    rude_keywords = ["shit", "fuck", "stupid", "idiot", "useless", "hate", "boring", "dumb", "worst"]
    if any(rude in t for rude in rude_keywords):
        return "Sorry if something upset you. Let me know how I can support you—or want a joke, a motivational quote, or a safe space to vent?"

    # Direct requests for jokes
    if "joke" in t:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😂",
            "Why did the math book look sad? Because it had too many problems! 🤓",
            "Why do bicycles fall over? Because they are two-tired! 🚲",
            "Why did the computer go to therapy? It had too many bytes of sadness! 💻"
        ]
        return random.choice(jokes)

    # Motivation / confidence
    motivate_keywords = ["motivate", "confidence", "motivation", "inspire", "courage", "boost", "encourage"]
    if any(word in t for word in motivate_keywords):
        motivates = [
            "You are stronger and smarter than your hardest day. You’re doing great! 💪",
            "Mistakes are proof that you are trying. Step by step, you’ll get there.",
            "You matter, and your best is enough. The world is better with you in it!"
        ]
        return random.choice(motivates)

    # Sad/down support
    sad_words = ["sad", "depressed", "lonely", "upset", "down", "pain", "tired", "cry", "trouble", "lost"]
    if any(word in t for word in sad_words):
        sad_replies = [
            "I'm sorry you feel that way. If you want to talk about it or need a little distraction, I’m here. 💜",
            "Tough times never last, but tough people do! If you need, I can suggest a calming exercise or tell a joke.",
            "You’re not alone: if talking helps, I’m ready to listen. Want a motivation or something fun?"
        ]
        return random.choice(sad_replies)

    # Help/support/advice
    help_words = ["help", "support", "listen", "advice", "stuck", "problem", "issue", "confused"]
    if any(word in t for word in help_words):
        help_replies = [
            "I'm happy to help! Let me know more, or ask for advice, motivation, or a joke.",
            "Sometimes describing your problem helps find a solution—I'm listening.",
            "Would talking to a trusted friend or family help too? I'm always here to talk."
        ]
        return random.choice(help_replies)

    # Happy/positive
    happy_words = ["happy", "awesome", "excited", "good", "joy", "fun", "fantastic", "glad", "cheerful"]
    if any(word in t for word in happy_words):
        return "That’s fantastic! Keep enjoying and spreading the happiness—if you want to share more, I’m listening! 😊"

    # Thank you/Gratitude
    if any(x in t for x in ["thanks", "thank you", "thx", "grateful", "appreciate"]):
        return "You're always welcome! If you need a joke, advice, or just a friend to chat, just ask."

    # Greetings
    if any(x in t for x in ["hello", "hi", "hey", "namaste"]):
        return "Hello! 😊 How are you feeling right now? Want a joke, motivation, or to just talk?"

    # Who are you?
    if "who are you" in t:
        return "I'm your friendly chatbot—here to listen, motivate, cheer up, and be your safe buddy online! 🤗"

    # Direct questions
    if t.endswith("?") or any(q in t for q in ["what", "why", "how", "when", "where", "who"]):
        return "That’s a great question! I’m designed for support, motivation, and jokes. You can ask for advice, a mood boost, or just share what’s on your mind."

    # Fallback
    fallback = [
        "I’m here to support you with a joke, motivation, advice, or just company. Tell me how can I help! 😊",
        "I'm always here if you want to talk or need cheering up. Just ask for a joke or inspiration!",
        "Let's talk—share something you're thinking about, or type 'joke', 'motivate', or 'help' for what you need."
    ]
    return random.choice(fallback)

@app.post("/chat/")
def chat(message: Message):
    reply = get_reply(message.text)
    return {"reply": reply}