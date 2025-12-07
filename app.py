from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LINE_TOKEN = "你的 LINE Channel Access Token"

charImages = {
    "奈芙爾": "https://upload-os-bbs.hoyolab.com/upload/2025/10/22/248396204/03efcd616004083b56f1236291a8168c_1765848458562635549.jpg",
    "菲林斯": "https://upload-os-bbs.hoyolab.com/upload/2025/09/29/248396204/86565129968b752c57f54294a09f2274_8369161948052686452.jpg",
}

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Received from LINE:", data)

    events = data.get("events", [])
    for event in events:
        reply_token = event["replyToken"]
        user_message = event["message"]["text"]
        image_url = charImages.get(user_message, "")
        text_reply = f"{user_message} 的培養攻略" if image_url else "找不到這個角色"

        payload = {
            "replyToken": reply_token,
            "messages": [
                {"type": "text", "text": text_reply},
            ]
        }

        if image_url:
            payload["messages"].append({
                "type": "image",
                "originalContentUrl": image_url,
                "previewImageUrl": image_url
            })

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {LINE_TOKEN}"
        }

        requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=payload)

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
