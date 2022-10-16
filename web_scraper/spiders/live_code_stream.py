import scrapy
class LiveScoreT(scrapy.Spider):
    name = "LiveScoreT"

    start_urls = [
        "https://livescore.cz/"
    ]

    def parse(self, response):
        yield {
            'tournament': response.xpath("/html/body/text()").get()
        }

#//*[@id="score-data"]
# /html/body/div[3]/div
#/html/body/div[3]/div
