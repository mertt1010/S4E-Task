from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS modülünü içeri aktar
import subprocess

app = Flask(__name__)
CORS(app)  # CORS'u tüm API'ye uyguladık

@app.route('/generate_code', methods=['POST'])
def generate_code():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    result = subprocess.run(['ollama', 'run', 'meta-llama', prompt], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        code_output = result.stdout.decode('utf-8')
        return jsonify({'code': code_output}), 200
    else:
        return jsonify({'error': result.stderr.decode('utf-8')}), 500

if __name__ == '__main__':
    app.run(debug=True)
