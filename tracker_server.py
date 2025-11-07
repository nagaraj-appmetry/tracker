from flask import Flask, send_file, request
import logging
from datetime import datetime
import sys


app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("opens.log"),         # Save logs to file (optional)
        logging.StreamHandler(sys.stdout)         # ✅ This sends logs to Render console
    ]
)

@app.route("/track/<tracking_id>.png")
def track_open(tracking_id):
    ip = request.remote_addr
    ua = request.headers.get("User-Agent", "")
    logging.info(f"Email opened — Tracking ID: {tracking_id}, IP: {request.remote_addr}")
    return send_file("pixel.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
