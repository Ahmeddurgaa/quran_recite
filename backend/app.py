from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    # Simulated recognition result
    next_verse_audio = random.choice([
        "https://download.quranicaudio.com/qdc/abdul_basit/murattal/001002.mp3",
        "https://download.quranicaudio.com/qdc/abdul_basit/murattal/001003.mp3"
    ])
    return jsonify({"next_audio": next_verse_audio})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
