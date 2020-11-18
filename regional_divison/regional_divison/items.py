# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RegionalDivisonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area = scrapy.Field()
    area_code = scrapy.Field()
    area_url = scrapy.Field()
