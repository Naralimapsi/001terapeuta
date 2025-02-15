
import requests
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Message is required."}), 400
    
    # Configuração da API
    api_url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',  # Aqui é onde você coloca a chave da API
    }
    
    payload = {
        'model': 'gpt-4',  # Defina o modelo que você está usando
        'messages': [
            {'role': 'user', 'content': user_message},
        ]
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "API error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
