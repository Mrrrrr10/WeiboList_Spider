# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboListSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# ---------- Item_WeiboUser ----------
class WeiboUserItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    avatar = scrapy.Field()
    cover = scrapy.Field()
    gender = scrapy.Field()
    description = scrapy.Field()
    fans_count = scrapy.Field()
    follows_count = scrapy.Field()
    weibos_count = scrapy.Field()
    verified = scrapy.Field()
    verified_reason = scrapy.Field()
    verified_type = scrapy.Field()
    follows = scrapy.Field()
    fans = scrapy.Field()
    crawled_at = scrapy.Field()


class WeiboUserRelationItem(scrapy.Item):
    id = scrapy.Field()
    follows = scrapy.Field()
    fans = scrapy.Field()
    crawled_at = scrapy.Field()


class WeiboItem(scrapy.Item):
    id = scrapy.Field()
    attitudes_count = scrapy.Field()
    comments_count = scrapy.Field()
    reposts_count = scrapy.Field()
    picture = scrapy.Field()
    pictures = scrapy.Field()
    source = scrapy.Field()
    text = scrapy.Field()
    raw_text = scrapy.Field()
    thumbnail = scrapy.Field()
    user = scrapy.Field()
    created_at = scrapy.Field()
    crawled_at = scrapy.Field()
    follows = scrapy.Field()
    fans = scrapy.Field()
