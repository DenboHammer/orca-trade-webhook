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
    data = request.get_json(force=True)

    # Формируем сообщение для Telegram
    text = (
        f"⚡ <b>Flip Signal</b>\n\n"
        f"Direction: <b>{data.get('dir')}</b>\n"
        f"Symbol: <b>{data.get('symbol')}</b>\n"
        f"Timeframe: <b>{data.get('tf')}</b>\n"
        f"Price: <b>{data.get('price')}</b>"
    )

    # Отправляем сообщение в Telegram
    requests.post(TG_URL, data={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    })

    return "ok", 200
