import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import HummusItem

class HumspiderSpider(CrawlSpider):
    custom_settings = {"CLOSEDSPIDER_ITEMCOUNT": 250,
                       "CLOSEDSPIDER_PAGECOUNT": 2 } # hopefully this limits the number of scraped items

    name = "humspider"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php?type=airing"]

    rules = (Rule(LinkExtractor(allow=r"/anime"), callback="parse_item", follow=True),
             # Rule(LinkExtractor(allow=r"/anime"), ) does this allow you to extract the ranks from the first page??
               )

    def parse_item(self, response):
        load = ItemLoader(item=HummusItem(), response=response)
        load.add_css("title", "div[itemprop=name] p.title-english.title-inherit")
        load.add_css("score", "div.score-label.score-8")
        load.add_css("season", "div.information-block.di-ib.clearfix span.information.season a")
        load.add_css("type", "div.information-block.di-ib.clearfix span.information.type a")
        load.add_css("plot", "td[valign=top] p[itemprop=description]")
        return load.load_item()
        """
        1."::text" (anime english name)
            query the element > space for searching for element > add . when theres is space btw class or id > ::text to get the text of said element
        2. ::text (anime score)

        3. ::text ( season)

        4. ::text" (type)

        5. ::text (anime plot)
        """
      
#TODO: find css seelctors for the name, rating/ rank, score  /DONE

#TODO: idea is to combine different anime scores and get the plots too, just incase... /DONE
    
#TODO: find out if you can have different spiders for the same crawler[reduce stress wehn extracting animes] /you cannot