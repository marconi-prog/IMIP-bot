import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv() # Carrega a chave do arquivo .env

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def pedir_desafio_ia(idade):
    prompt = f"""
    Aja como um professor lúdico para uma criança de {idade} anos em um hospital.
    Gere um objeto simples de 4 a 6 letras.
    Retorne APENAS um JSON no formato:
    {{"palavra": "BOLA", "dica": "Cuidado para não chutar no corredor!", "personagem_disse": "Oi amiguinho! Consegue completar essa?"}}
    """
    
    response = model.generate_content(prompt)
    # Limpa a resposta para garantir que seja um JSON puro
    data = json.loads(response.text.replace('```json', '').replace('```', ''))
    return data