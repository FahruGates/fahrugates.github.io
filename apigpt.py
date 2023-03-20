import openai
import json
from flask import Flask, request

app = Flask(__name__)

# Masukkan API key OpenAI
openai.api_key = "keyless"

# Fungsi untuk mengirim permintaan ke model GPT
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()

# Route untuk mengirim dan menerima pesan dari sisi klien
@app.route('/chat', methods=['POST'])
def chat():
    req_data = request.get_json()
    message = req_data['message']
    response = generate_text(message)
    return json.dumps({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
