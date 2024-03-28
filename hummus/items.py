# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import MapCompose, TakeFirst

class HummusItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(input_processor=MapCompose(remove_tags, ),
                         output_processor=TakeFirst())
    
    score  = scrapy.Field(input_processor=MapCompose(remove_tags, ),
                          output_processor=TakeFirst())
    
    rank = scrapy.Field(input_processor=MapCompose(remove_tags, ),
                        output_processor=TakeFirst())
    
    season = scrapy.Field(input_processor=MapCompose(remove_tags, ),
                          output_processor=TakeFirst())
    
    type = scrapy.Field(input_processor=MapCompose(remove_tags, ),
                        output_processor=TakeFirst())
    
    plot = scrapy.Field(input_processor=MapCompose(remove_tags, ),
                        output_processor=TakeFirst())
    
    