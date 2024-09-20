import scrapy

class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com']
    start_urls = ['http://google.com/']

    def parse(self, response):
        # 使用XPath或CSS选择器提取标题
        title = response.xpath('//title/text()').get()
        yield {'title': title}

