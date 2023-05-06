import scrapy
import json

class TOJSONSpider(scrapy.Spider):
    name = "toJSON"
    with open('links.json', 'r') as json_file:
        data = json.load(json_file)

    start_urls = list(data.values())
    print("start_urls-Variable: ", start_urls) 
    #start_urls = [
        #'https://quotes.toscrape.com/page/1/',
        #'https://quotes.toscrape.com/page/2/',
    #]

    def parse(self, response):
        textJSON = response.xpath('//*[@class="_5pbx userContent _3576"]//p//text()').getall()
        print("Ausgabetext: ", textJSON)
        with open('data.json', 'w') as file:
            json.dump(textJSON, file)
        
