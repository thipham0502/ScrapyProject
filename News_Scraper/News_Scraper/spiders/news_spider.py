import scrapy

# Spider class
class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        # "https://vnexpress.net/giai-tri/nhac-p1",
        # "https://vnexpress.net/giai-tri/nhac-p2"
        "https://www.billboard.com/k-pop",
        "https://www.billboard.com/pop",
        "https://www.billboard.com/hip-hop-rap-r-and-b",
        "https://www.billboard.com/dance"
    ]

    def parse(self, response):
        page = response.url.split('-p')[-1]
        # filename = 'news.csv'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for title_news in response.css('.news-feed-article'):
            title = title_news.css('h2 a::text').get()
            yield {'title':title}