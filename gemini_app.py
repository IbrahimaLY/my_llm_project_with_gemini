# Fichier : gemini_app.py (Vérification avant l'instanciation)

import os
from google import genai
from dotenv import load_dotenv

load_dotenv() 

google_api_key = os.getenv('GEMINI_API_KEY')

if not google_api_key:
    print("❌ Erreur : La variable d'environnement GEMINI_API_KEY n'a pas été trouvée. Vérifiez votre fichier .env.")
else:
    print("Clé API trouvée. Instanciation du client.")
    # Passez la clé explicitement ou laissez genai.Client() la trouver
    client = genai.Client(api_key=google_api_key) 
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explique comment l'IA fonctionne en quelques mots, sous forme de citation percutante."
    )
    print("\nRéponse de Gemini :")
    print(response.text)