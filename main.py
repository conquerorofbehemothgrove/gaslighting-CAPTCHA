from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Dictionary to force correct words into incorrect ones
# Replace just the TYPO_MAP section in your main.py
TYPO_MAP = {
    "their": "there",
    "there": "they're",
    "they're": "their",
    "definitely": "definately",
    "separate": "seperate",
    "receive": "recieve",
    "literally": "litterally",
    "too": "to",
    "to": "too",
    "its": "it's",
    "it's": "its",
    "weird": "wired",
    "independent": "independant",
    "accommodate": "acommodate",
    "you're": "your",
    "your": "you're",
    "affect": "effect",
    "effect": "affect",
    "lose": "loose",
    "loose": "lose",
    "accept": "except",
    "except": "accept",
    "necessary": "neccessary",
    "tomorrow": "tommorow",
    "privilege": "privelege",
    "successful": "succesful",
    "occurrence": "occurence"
}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enforce', methods=['POST'])
def enforce_typos():
    data = request.json or {}
    text = data.get('text', '')

    words = text.split(' ')
    modified_words = []
    
    for word in words:
        clean_word = word.lower().strip(',.?!')
        if clean_word in TYPO_MAP:
            # Swap the word with its typo equivalent
            typo = TYPO_MAP[clean_word]
            # Naively restore basic punctuation 
            if word.endswith(','): typo += ','
            elif word.endswith('.'): typo += '.'
            modified_words.append(typo)
        else:
            modified_words.append(word)

    return jsonify({"text": " ".join(modified_words)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
