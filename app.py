from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return "IHAAN Body Running"

@app.route("/goal")
def goal():
    scrape_value = request.args.get("scrape")

    if scrape_value == "example":
        url = "https://example.com"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return f"Result: {soup.title.string}"

    return "No valid goal provided"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
