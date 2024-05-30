from flask import Flask, request, jsonify
import sys
import os

# Add the project's root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.chatbot import generate_response

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    prompt = data['prompt']
    response = generate_response(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
