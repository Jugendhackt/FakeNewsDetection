from scrapy.spiders import Spider


class ImdbSpider(Spider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/']

    def parse(self, response):
        pass
