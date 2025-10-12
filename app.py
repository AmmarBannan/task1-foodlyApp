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

    result = "Hello from Foodly in Docker!"
    result += "<br>Log file date+time (until second space):"

    try:
        with open("logs/app.log", "r") as f:
            for line in f:
                parts = line.split(" ", 2) 
                if len(parts) >= 2:
                    datetime_str = parts[0] + " " + parts[1]
                    result += f"<br>{datetime_str}"
                else:
                    result += f"<br>{line.strip()}"
    except FileNotFoundError:
        result += "<br>No logs found yet."

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Dockerfile 7