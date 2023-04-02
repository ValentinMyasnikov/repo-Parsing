import scrapy


class BookSpiderSpider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/index.html']

    def parse(self, response):
        for link in response.xpath("//article[@class='product_pod']/h3/a/@href"):
            yield response.follow(link, callback=self.parse_book)

        for i in range(1, 50):
            next_page = f'https://books.toscrape.com/catalogue/page-{i}.html'
            yield response.follow(next_page, callback=self.parse)


    def parse_book(self, response):
        yield {
        'name': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
        'price': response.xpath("//p[@class='price_color']/text()").get(),
        'in_stock': response.xpath("//p[@class='instock availability']/text()")[1].get().strip(),
        'UPC': response.xpath("//table[@class='table table-striped']/tr/td/text()").get()
  }