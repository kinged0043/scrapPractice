import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import HummusItem

class HumspiderSpider(CrawlSpider):
    name = "humspider"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php?type=airing"]

    rules = (Rule(LinkExtractor(allow=r"/anime"), callback="parse_item", follow=True),
             # Rule(LinkExtractor(allow=r"/anime"), ) does this allow you to extract the ranks from the first page??
               )

    def parse_item(self, response):
        # load = ItemLoader(item=I temLoader(), response=response)
        # load.add_css("rank", "")
        # load.add_css("rank", "")
        # load.add_css("rank", "")
        # load.add_css("rank", "")
        # load.add_css("rank", "")
        # return load.load_item()
        """
        1."div[itemprop=name] p.title-english.title-inherit::text" (anime english name)
            query the element > space for searching for element > add . when theres is space btw class or id > ::text to get the text of said element
        2. div.score-label.score-8::text (anime score)

        3. div.information-block.di-ib.clearfix span.information.season a::text ( season)

        4. div.information-block.di-ib.clearfix span.information.type a::text" (type)

        5. td[valign=top] p[itemprop=description]::text (anime plot)
        """
        yield {
            'rank': response.css("tr.ranking-list span.lightLink.top-anime-rank-text.rank1::text"),
            'title': response.css("div[itemprop=name] p.title-english.title-inherit::text").get(),
            'score': response.css("div.score-label.score-8::text").get(),
            'season': response.css("div.information-block.di-ib.clearfix span.information.season a::text").get(),
            'type': response.css("div.information-block.di-ib.clearfix span.information.type a::text").get(),
            'plot': response.css("td[valign=top] p[itemprop=description]::text").get()
            }

#TODO: find css seelctors for the name, rating/ rank, score  /DONE

#TODO: idea is to combine different anime scores and get the plots too, just incase... /DONE
    
#TODO: find out if you can have different spiders for the same crawler[reduce stress wehn extracting animes] /you cannot