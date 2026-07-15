import requests
from bs4 import BeautifulSoup
import urllib.parse


# ===================================
# Function to Scrape Wikipedia Summary
# ===================================
def wikipedia_summary(query):
    try:
        query = urllib.parse.quote(query.replace(" ", "_"))

        url = f"https://en.wikipedia.org/wiki/{query}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return "Sorry, I couldn't find information about that."

        soup = BeautifulSoup(response.text, "html.parser")

        content = soup.find("div", class_="mw-parser-output")

        if content is None:
            return "No summary found."

        paragraphs = content.find_all("p")

        summary = ""

        for paragraph in paragraphs:
            text = paragraph.get_text().strip()

            if len(text) > 80:
                summary = text
                break

        if summary == "":
            return "No useful information found."

        return summary

    except Exception:
        return "Unable to connect to Wikipedia."


# ===================================
# Rule-Based Responses
# ===================================
responses = {

    "hello":
        "Hello! How can I help you today?",

    "hi":
        "Hi! Nice to meet you.",

    "hey":
        "Hey! What can I do for you?",

    "how are you":
        "I'm doing great. Thanks for asking!",

    "your name":
        "I'm an Intelligent Rule-Based Assistant.",

    "who are you":
        "I am a Python chatbot created for your assignment.",

    "what can you do":
        "I can answer basic questions and search Wikipedia for unknown topics.",

    "python":
        "Python is a powerful programming language used in AI, web development, automation, and data science.",

    "ai":
        "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",

    "bye":
        "Goodbye! Have a wonderful day.",

    "thanks":
        "You're welcome!",

    "thank you":
        "Glad I could help!"
}


# ===================================
# Chatbot
# ===================================
print("=" * 60)
print(" Intelligent Rule-Based Assistant ")
print("=" * 60)
print("Type 'bye' or 'exit' to quit.\n")

while True:

    user_input = input("You: ").strip().lower()

    if user_input in ["bye", "exit", "quit"]:
        print("Bot:", responses["bye"])
        break

    found = False

    for key in responses:

        if key in user_input:
            print("Bot:", responses[key])
            found = True
            break

    if not found:

        print("Bot: I don't know much about that.")
        print("Searching Wikipedia...\n")

        summary = wikipedia_summary(user_input)

        print(summary)
        print()