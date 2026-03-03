from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return "IHAAN Body Running"

@app.route("/goal", methods=["POST"])
def goal():
    data = request.get_json()
    goal_text = data.get("goal", "")

    if "scrape example" in goal_text.lower():
        url = "https://example.com"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string
        return jsonify({"status": "completed", "result": title})

    return jsonify({"status": "unknown goal"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
