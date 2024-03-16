import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HumspiderSpider(CrawlSpider):
    name = "humspider"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php?type=airing"]

    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item

#TODO: find css seelctors for the name, rating/ rank, score  

#TODO: idea is to combine different anime scores and get the plots too, just incase...
    
#TODO: find out if you can have different spiders for the same crawler[reduce stress wehn extracting animes]