from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import datetime

app = Flask(__name__)

logs = []

def log_event(event):
    logs.append({
        "time": str(datetime.datetime.now()),
        "event": event
    })

@app.route("/")
def home():
    return "IHAAN Body Running"

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
    url = data.get("url")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No title found"

        log_event(f"Scraped {url}")

        return jsonify({
            "status": "success",
            "title": title
        })

    except Exception as e:
        log_event(f"Error scraping {url}")
        return jsonify({
            "status": "error",
            "message": str(e)
        })

@app.route("/logs")
def get_logs():
    return jsonify(logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
