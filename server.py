from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TG_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"


@app.route("/", methods=["GET"])
def home():
    return "OrcaTrade Webhook is running!", 200


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True) or {}

    # ✅ Если Pine прислал готовый текст — используем его
    if data.get("text"):
        text = data["text"]
        parse_mode = None  # обычный текст (как в popup)
    else:
        # fallback (на случай если text не пришёл)
        text = (
            f"⚡ <b>Flip Signal</b>\n\n"
            f"Direction: <b>{data.get('dir')}</b>\n"
            f"Symbol: <b>{data.get('symbol')}</b>\n"
            f"Timeframe: <b>{data.get('tf')}</b>\n"
            f"Price: <b>{data.get('price')}</b>"
        )
