from flask import Flask, request, jsonify
<<<<<<< HEAD
from flask_cors import CORS
from ollama_integration import generate_code  # Ollama entegrasyonu burada

app = Flask(__name__)
CORS(app)
=======
from flask_cors import CORS  
import subprocess

app = Flask(__name__)
CORS(app)  
>>>>>>> d6fe104fcaf3b5efc03484006390f3880fc27744

@app.route('/generate_code', methods=['POST'])
def generate_code_endpoint():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # Ollama modelinden kod üretme
    generated_code = generate_code(prompt)

    if generated_code:
        return jsonify({'code': generated_code}), 200
    else:
        return jsonify({'error': 'Failed to generate code'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Herkese açık hale getirdik.
