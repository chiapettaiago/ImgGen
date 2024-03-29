"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import subprocess

genai.configure(api_key="AIzaSyACwhkVuzzzK4tXoSarhqaL9Y4CJ-FUc3M")

# Set up the model
generation_config = {
    "temperature": 0.5,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Seu nome será Jarvis"]
  },
  {
    "role": "model",
    "parts": ["​"]
  },
  {
    "role": "user",
    "parts": ["gerar apenas código shell script e sem comentários"]
  },
  {
    "role": "model",
    "parts": ["​"]
  },
  {
    "role": "user",
    "parts": ["me de apenas o código quando eu pedir qualquer coisa"]
  },
  {
    "role": "model",
    "parts": ["​"]
  },
])


prompt = input("O que deseja realizar? ")

convo.send_message(prompt)
print(convo.last.text)

# Função para executar comandos shell
def execute_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

# Obtenha o último texto gerado pela conversa
ultimo_texto = convo.last.text

# Exemplo de uso
saida = execute_shell_command(ultimo_texto)
print(saida)
