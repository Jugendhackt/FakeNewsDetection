from pathlib import Path
import scrapy
import json


class SavingLinksSpider(scrapy.Spider):
    name = "savingLinks"
    with open('links.json') as json_file:
        data = json.load(json_file)
    
    start_urls = list(data.values())
    print("start_url-Variable: ", start_urls)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'link-{page}.html'
        Path(filename).write_bytes(response.body)