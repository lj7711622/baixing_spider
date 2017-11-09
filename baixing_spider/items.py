# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaixingSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title 	= scrapy.Field()
    # 地址
    url   	= scrapy.Field()
    # 价格
    price 	= scrapy.Field()
    # 出租类型 ：整租、单间出租
    detail = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 发布时间
    publish_date = scrapy.Field()
    # 手机号
    mobile = scrapy.Field()
    #lng = 121.46621074903, lat = 31.241220278074; 
    lng = scrapy.Field()
    lat = scrapy.Field()