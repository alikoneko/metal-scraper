# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Band(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    style = scrapy.Field()
    country = scrapy.Field()
