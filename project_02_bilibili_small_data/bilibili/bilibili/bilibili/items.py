# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    mid = scrapy.Field()
    name = scrapy.Field()
    approve = scrapy.Field()
    sex = scrapy.Field()
    rank = scrapy.Field()
    face = scrapy.Field()
    coins = scrapy.Field()
    display_rank = scrapy.Field()
    regtime = scrapy.Field()
    spacesta = scrapy.Field()
    birthday = scrapy.Field()
    place = scrapy.Field()
    descrption = scrapy.Field()
    article = scrapy.Field()
    attentions = scrapy.Field()
    fans = scrapy.Field()
    friend = scrapy.Field()
    attention = scrapy.Field()
    # 签名
    sign = scrapy.Field()
    current_level = scrapy.Field()
    current_exp = scrapy.Field()
    play_num = scrapy.Field()
    pass
