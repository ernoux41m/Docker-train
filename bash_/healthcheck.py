# healthcheck.py

import requests
import sys

def check_health():
    try:
        response = requests.get('https://www.example.com')  # Remplacez l'URL par celle de votre application
        if response.status_code == 200:
            return 0  # Tout va bien
        else:
            return 1  # Il y a un problème
    except requests.RequestException:
        return 1  # Erreur lors de la requête

if __name__ == "__main__":
    sys.exit(check_health())
