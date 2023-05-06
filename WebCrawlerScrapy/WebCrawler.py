import requests
from bs4 import BeautifulSoup
import json
import datetime
import os

urls = [
    search_item_list
]

searched_keyword = "Brexit"
searched_keyword_string = "Suchanfrage:"

def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        return response.text
    else:
        return None


def get_data(html, searcherd_term_key, searcherd_term_string):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    long_texts = [str(p.get_text().strip()) for p in paragraphs if len(p.get_text().split()) > 15]
    for text in long_texts:
        print(text)

    number_search = 5

    data = {
        f'Search {number_search}' :
        {
            searcherd_term_string : searcherd_term_key,
            'timestamp': str(datetime.datetime.now()),
            'long_texts': long_texts
        }
    }

    with open('data.json', 'r') as file:
        existing_data = json.load(file)

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=5) 


def check_Availability(file_path_Element):
    if os.access(file_path_Element, os.W_OK):
        print("Sie haben Schreibberechtigungen für den angegebenen Pfad.")
    else:
        ("Sie haben keine Schreibberechtigungen für den angegebenen Pfad.")

check_Availability('data.json')

def run_crawler(urls, searched_keyword, searched_keyword_string):
    html = get_page(urls)
    if html is None:
        print("Fehler beim Abrufen der Startseite.")
        return
    page_text = get_data(html, searched_keyword, searched_keyword_string)
    if page_text != None:
        print('Es funktioniert...')
    else: print('Kein Inhalt mehr... ')

for url in urls:
    for lol in url:
        run_crawler(url, searched_keyword, searched_keyword_string)