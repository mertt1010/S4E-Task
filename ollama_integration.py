import subprocess

def generate_code(prompt):
    """
    Bu fonksiyon, Ollama modelini kullanarak verilen prompt'a göre Python kodu üretir.
    """
    try:
        result = subprocess.run(['ollama', 'run', 'meta-llama', prompt], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout.decode('utf-8')  
            return f"Hata: {result.stderr.decode('utf-8')}"  
    except Exception as e:
        return f"Exception occurred: {str(e)}"  
