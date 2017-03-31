# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:

    rate = scrapy.Field()
    cover_x = scrapy.Field()
    is_beetle_subject = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    playable = scrapy.Field()
    cover = scrapy.Field()
    id = scrapy.Field()
    cover_y = scrapy.Field()
    is_new = scrapy.Field()
    body = scrapy.Field()
    create_time = scrapy.Field()

    director        = scrapy.Field()
    scriptwriter    = scrapy.Field()
    actor           = scrapy.Field()
    type            = scrapy.Field()
    country         = scrapy.Field()
    language        = scrapy.Field()
    uptime          = scrapy.Field()
    anthorname      = scrapy.Field()
    imdblink        = scrapy.Field()
    summary         = scrapy.Field()
    hotjudge        = scrapy.Field()
    sorce           = scrapy.Field()

    pass
