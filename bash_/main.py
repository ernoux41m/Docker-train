import os
import requests
import time

def main():
    
    name = os.getenv('NAME', 'Matthieu Ernoux')  

    while True:
        response = requests.get('https://www.google.com')  
        print(f"{name} a reçu une réponse : {response.status_code}")
        time.sleep(5)  

if __name__ == "__main__":
    main()
