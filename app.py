from flask import Flask, request
import logging
import os

app = Flask(__name__)

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def home():
    logging.info("Request received at / from %s", request.remote_addr)
    return "Hello from Foodly in Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
