import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN") 
BASE = f"https://botapi.rubika.ir/v3/{TOKEN}"

def send(chat_id, text):
    try:
        requests.post(f"{BASE}/sendMessage", json={"chat_id": chat_id, "text": text}, timeout=10)
    except Exception as e:
        print("خطا در ارسال:", e)

@app.route("/", methods=["GET"])
def home():
    return "ربات روشنه!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if not data:
        return "OK", 200
        
    if data.get("type") == "NewMessage":
        msg = data.get("new_message", {})
        chat_id = data.get("chat_id")
        text = msg.get("text", "").strip()
        
        if not text:
            return "OK", 200
            
        if text == "/start":
            send(chat_id, "سلام!\n1 سفارش\n2 تبلیغ ساعتی\n3 تعرفه\n4 پشتیبانی\n5 قوانین\n6 درباره ما")
        elif text == "1": send(chat_id, "📢 سفارش تبلیغ")
        elif text == "2": send(chat_id, "⏱️ تبلیغ ساعتی")
        elif text == "3": send(chat_id, "💰 تعرفه‌ها")
        elif text == "4": send(chat_id, "📞 @crative017")
        elif text == "5": send(chat_id, "📜 قوانین")
        elif text == "6": send(chat_id, "ℹ️ درباره ما")
        
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
