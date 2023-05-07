import requests
from bs4 import BeautifulSoup
import json
import datetime
import search
import os

query = 'Künstliche Intelligenz'

urls = search.search_(query)

searched_keyword = "Suchanfrage:"
searched_keyword_string = query

def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        return response.text
    else:
        return None


def bypass_cookies_banner(url):
    session = requests.Session()
    response = session.get(url)
    cookies = response.cookies 
    session.cookies.set('consent_cookie', 'accepted', domain=url)
    response = session.get(url)
    print("Cookiebanner wurde umgangen!")

def get_data(html, searcherd_term_key, searcherd_term_string):
    soup = BeautifulSoup(html, 'html.parser')
    p_text = soup.find_all('p')
    h1_text = soup.find_all('h1')
    h2_text = soup.find_all('h2')
    h3_text = soup.find_all('h3')
    h4_text = soup.find_all('h4')
    h5_text = soup.find_all('h5')
    h6_text = soup.find_all('h6')
    long_texts = []
    h_texts = []
    for p in p_text:
        p_text = p.get_text().strip()
        if len(p_text.split()) > 15:    
            long_texts.append(p_text)
            print("Neues P-Element hinzugefügt!")
        else:
            print("Element ist schon in 'long_texts' vorhanden!")
    for h in h1_text:
        h1_text = h.get_text().strip()
        if h1_text not in h_texts:
            h_texts.append(h1_text)
            print("Neues H-Element hinzugefügt")
        else:
            print("H-Element ist schon ist schon in 'h_texts' vorhanden!")
    for h in h2_text:
        h2_text = h.get_text().strip()
        if h2_text not in h_texts:
            h_texts.append(h2_text)
            print("Neues H-Element hinzugefügt")
        else:
            print("H-Element ist schon ist schon in 'h_texts' vorhanden!")
    for h in h3_text:
        h3_text = h.get_text().strip()
        if h3_text not in h_texts:
            h_texts.append(h3_text)
            print("Neues H-Element hinzugefügt")
        else:
            print("H-Element ist schon ist schon in 'h_texts' vorhanden!")
    for h in h4_text:
        h4_text = h.get_text().strip()
        if h4_text not in h_texts:
            h_texts.append(h4_text)
            print("Neues H-Element hinzugefügt")
        else:
            print("H-Element ist schon ist schon in 'h_texts' vorhanden!")
    for h in h5_text:
        h5_text = h.get_text().strip()
        if h5_text not in h_texts:
            h_texts.append(h5_text)
            print("Neues H-Element hinzugefügt")
        else:
            print("H-Element ist schon ist schon in 'h_texts' vorhanden!")
    for h in h6_text:
        h6_text = h.get_text().strip()
        if h6_text not in h_texts:
            h_texts.append(h6_text)
            print("Neues H-Element hinzugefügt")
        else:
            print("H-Element ist schon ist schon in 'h_texts' vorhanden!")


    for content1 in long_texts:
        print("PRINTING TEXT:   ")
        print(content1)
    for content2 in h_texts:
        print("PRINTING TEXT:   ")
        print(content2)

    data = {
        'Search':
        {
            searcherd_term_key : searcherd_term_string,
            'timestamp': str(datetime.datetime.now()),
            'long_texts': long_texts,
            'h_texts': h_texts
        }
    }

    with open('data.json', 'r') as file:
        existing_data = json.load(file)

    existing_data[searcherd_term_key] = (data)

    with open('data.json', 'w') as file:
        json.dump(existing_data, file, indent=5) 

    combinded_data_list = long_texts + h_texts
    formatted_data_list = [[item] for item in combinded_data_list]
    print(formatted_data_list)


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
    run_crawler(url, searched_keyword, searched_keyword_string)
    bypass_cookies_banner(url) 