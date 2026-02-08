print('Backend placeholder. Paste your real app.py here.')
# Quran Reciter - Minimal Working Example (Flutter + Flask)


This is a **minimal runnable version** that allows:
- Microphone recording in Flutter (web)
- Sending audio to backend
- Backend returns "next verse" trigger
- Flutter automatically plays the next verse audio


---


# Backend (backend/app.py)
```python
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
```


requirements.txt
```
flask
```


---
