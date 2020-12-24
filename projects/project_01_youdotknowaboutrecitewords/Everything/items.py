# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EverythingItem(scrapy.Item):

    user_id = scrapy.Field()

    username = scrapy.Field()
    nickname = scrapy.Field()

    growth_stat = scrapy.Field()
    words_count = scrapy.Field()
    words_learned_count = scrapy.Field()
    words_learning_count = scrapy.Field()
    words_new_count = scrapy.Field()

    checkin_days_count = scrapy.Field()

    pass



class ShanbayItem(scrapy.Item):

    user_id = scrapy.Field()

    username = scrapy.Field()
    nickname = scrapy.Field()

    growth_stat = scrapy.Field()
    words_count = scrapy.Field()
    words_learned_count = scrapy.Field()
    words_learning_count = scrapy.Field()
    words_new_count = scrapy.Field()

    checkin_days_count = scrapy.Field()

    pass
