import subprocess

def generate_code(prompt):
   
    result = subprocess.run(['ollama', 'run', 'meta-llama', prompt], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
 
    if result.returncode == 0:
        return result.stdout.decode('utf-8')
    else:
        return f"Hata: {result.stderr.decode('utf-8')}"


prompt = "Bir 'Hello World' Python kodu yaz."
code_output = generate_code(prompt)
print(code_output)
