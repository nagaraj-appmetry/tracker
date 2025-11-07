from flask import Flask, send_file, request
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(filename="opens.log", level=logging.INFO, format="%(asctime)s - %(message)s")

@app.route("/track/<tracking_id>.png")
def track_open(tracking_id):
    ip = request.remote_addr
    ua = request.headers.get("User-Agent", "")
    logging.info(f"OPENED: {tracking_id} | IP: {ip} | UA: {ua}")
    return send_file("pixel.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
