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
def track(tracking_id):
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent", "").lower()

    # Identify auto-loads and real opens
    if "googleimageproxy" in ua:
        event_type = "REAL OPEN (Gmail App/Web)"
    elif "bot" in ua or "proxy" in ua or "python" in ua:
        event_type = "AUTOMATED SCAN"
    elif ip.startswith("127.") or ip.startswith("10."):
        event_type = "INTERNAL / RENDER PING"
    else:
        event_type = "POSSIBLE HUMAN OPEN"

    logging.info(f"[{event_type}] Tracking ID: {tracking_id}, IP: {ip}, UA: {ua}")
    return send_file("pixel.png", mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
