import requests
from bs4 import BeautifulSoup
import json
import datetime

urls = "https://en.wikipedia.org/wiki/OpenAI"

def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        return response.text
    else:
        return None


def extract_long_texts(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    long_texts = [str(p.get_text().strip()) for p in paragraphs if len(p.get_text().split()) > 15]
    for text in long_texts:
        print(text)

    data = {
        'timestamp': str(datetime.datetime.now()),
        'long_texts': long_texts
    }

    with open('data.json', 'r') as file:
        existing_data = json.load(file)

    with open('data.json', 'w') as file:
        json.dump(long_texts, file, indent=4)

    import os

    file_path = 'data.json'  # Passe den Pfad entsprechend an

    if os.access(file_path, os.W_OK):
        print("Sie haben Schreibberechtigungen für den angegebenen Pfad.")
    else:
        ("Sie haben keine Schreibberechtigungen für den angegebenen Pfad.")

def run_crawler(urls):
    html = get_page(urls)
    if html is None:
        print("Fehler beim Abrufen der Startseite.")
        return
    page_text = extract_long_texts(html)
    if page_text != None:
        print('Es funktioniert...')
    else: print('Kein Inhalt mehr... ')

run_crawler(urls)