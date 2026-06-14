from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Random jokes
jokes = [
    "Why don't programmers like nature? It has too many bugs.",
    "Python developers don't byte, they hiss.",
    "I told my computer a joke, now it won't stop laughing.",
    "Why did the programmer quit his job? Because he didn't get arrays."
]

# Motivational quotes
quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Keep learning, keep growing.",
    "Consistency beats intensity.",
    "Every expert was once a beginner.",
    "Dream big and work hard."
]


def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! 👋 How can I help you today?"

    # Name
    elif "name" in user_input:
        return "My name is SimpleAI Bot 🤖"

    # How are you
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😊"

    # Time
    elif "time" in user_input:
        return f"⏰ Current time is {datetime.now().strftime('%I:%M %p')}"

    # Date
    elif "date" in user_input:
        return f"📅 Today's date is {datetime.now().strftime('%d-%m-%Y')}"

    # Weather
    elif "weather" in user_input:
        return "🌤️ I can't check live weather yet, but you can use a weather website."

    # Study / Learning
    elif "study" in user_input or "learn" in user_input:
        return "📚 Practice daily, build projects, and stay consistent."

    # Joke
    elif "joke" in user_input:
        return f"😂 {random.choice(jokes)}"

    # Motivation
    elif "motivation" in user_input or "quote" in user_input:
        return f"💡 {random.choice(quotes)}"

    # Calculator
    elif any(op in user_input for op in ["+", "-", "*", "/"]):
        try:
            result = eval(user_input)
            return f"🧮 Answer: {result}"
        except:
            return "❌ Please enter a valid mathematical expression."

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        return "👋 Goodbye! Have a great day."

    # Default
    else:
        return "🤔 Sorry, I don't understand that. Try asking something else."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_response():
    data = request.get_json()
    user_message = data["message"]

    response = chatbot_response(user_message)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)