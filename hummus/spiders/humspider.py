import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import HummusItem

class HumspiderSpider(CrawlSpider):
    name = "humspider"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php?type=airing"]

    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        name = "  h3 > a.hoverinfo_trigger::text"
        rank = " h3 > td.rank ac::text"
        score = " h3 > span.text on score-label score-9::text"
        description = ""
        
        item = ItemLoader(HummusItem())
        #item["domain_id"] = response.css().get()
        #item["name"] = response.css().get()
        #item["description"] = response.css().get()       
        return item

#TODO: find css seelctors for the name, rating/ rank, score  

#TODO: idea is to combine different anime scores and get the plots too, just incase...
    
#TODO: find out if you can have different spiders for the same crawler[reduce stress wehn extracting animes]