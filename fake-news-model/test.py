import requests
from bs4 import BeautifulSoup
import json

url = "https://www.bbc.com/news"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and "/politics" in href:
        links.append(href)

data = []
for link in links:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.find('div', {'class': 'story-body__inner'}).get_text()
    data.append({'link': link, 'text': text})

with open('data.json', 'w') as f:
    json.dump(data, f)
