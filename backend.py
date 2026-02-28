from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "sk-..."  # 👈 your OpenAI key


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a farming assistant for Indian farmers. Give short, practical answers about crops, soil, pests, and climate."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=100
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

