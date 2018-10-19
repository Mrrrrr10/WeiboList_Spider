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


# ---------- Item_WeiboTopic ----------
class WeiboHotSearchItem(scrapy.Item):
    topic_name = scrapy.Field()
    total = scrapy.Field()
    start_time = scrapy.Field()
    id = scrapy.Field()
    weibo_url = scrapy.Field()
    text = scrapy.Field()
    source = scrapy.Field()
    created_at = scrapy.Field()
    reposts_count = scrapy.Field()  # 转发
    comments_count = scrapy.Field()  # 评论
    attitudes_count = scrapy.Field()  # 点赞
    review_count = scrapy.Field()
    video_link = scrapy.Field()
    user_id = scrapy.Field()
    username = scrapy.Field()
    gender = scrapy.Field()
    statuses_count = scrapy.Field()
    verified_reason = scrapy.Field()
    followers_count = scrapy.Field()
    follow_count = scrapy.Field()
    description = scrapy.Field()
    comment_info = scrapy.Field()
    comment_list = scrapy.Field()
    crawled_at = scrapy.Field()


class WeiboTopicListItem(scrapy.Item):
    topic_name = scrapy.Field()
    reading_volume = scrapy.Field()
    total = scrapy.Field()
    start_time = scrapy.Field()
    id = scrapy.Field()
    weibo_url = scrapy.Field()
    text = scrapy.Field()
    source = scrapy.Field()
    created_at = scrapy.Field()
    reposts_count = scrapy.Field()  # 转发
    comments_count = scrapy.Field()  # 评论
    attitudes_count = scrapy.Field()  # 点赞
    review_count = scrapy.Field()
    video_link = scrapy.Field()
    user_id = scrapy.Field()
    username = scrapy.Field()
    gender = scrapy.Field()
    statuses_count = scrapy.Field()
    verified_reason = scrapy.Field()
    followers_count = scrapy.Field()
    follow_count = scrapy.Field()
    description = scrapy.Field()
    comment_info = scrapy.Field()
    comment_list = scrapy.Field()
    crawled_at = scrapy.Field()


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
