# Fichier : gemini_app.py

from google import genai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv() 

# Le client va chercher automatiquement la clé dans GEMINI_API_KEY
client = genai.Client() 

# Assurez-vous que la clé a été chargée (bonne pratique)
if not client._client._credentials:
    print("Erreur : La variable d'environnement GEMINI_API_KEY n'est pas chargée.")
else:
    print("Clé API chargée avec succès.")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explique comment l'IA fonctionne en quelques mots, sous forme de citation percutante."
    )
    print("\nRéponse de Gemini :")
    print(response.text)