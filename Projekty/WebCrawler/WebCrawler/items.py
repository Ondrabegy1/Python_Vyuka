# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    item = scrapy.Field()
    price = scrapy.Field()
    priceBefore = scrapy.Field()
    discount = scrapy.Field()