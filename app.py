from flask import Flask, request, jsonify

app = Flask(__name__)

charImages = {
    "奈芙爾": "https://example.com/images/neuvillette.png",
    "甘雨": "https://example.com/images/ganyu.png",
}

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    character = data.get("character")  # 從你的聊天機器人接收角色名
    image_url = charImages.get(character, "")
    return jsonify({"message": f"{character} 的培養圖", "image_url": image_url})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
