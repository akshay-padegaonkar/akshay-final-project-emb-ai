"""Flask server for Emotion Detection API."""
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def main():
    return "Emotion Detection API running"

@app.route("/emotionDetector", methods=["POST"])
"""Handle emotion detection requests."""
def detect_emotion():
    data = request.get_json()
    text = data.get("text","")
    result = emotion_detector(text)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
