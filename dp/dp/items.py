# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DpItem(scrapy.Item):
    city = scrapy.Field()     # 城市
    name = scrapy.Field()     # 店铺名称
    address = scrapy.Field()  # 店铺地址
    district = scrapy.Field() # 店铺所在区域
    plate = scrapy.Field()    # 店铺所在板块
    type = scrapy.Field()     # 店铺类型
    classify = scrapy.Field() # 店铺分类
    url = scrapy.Field()      # 店铺url
    comment_number = scrapy.Field()  # 点评数
    comsume = scrapy.Field()  # 人均
    taste = scrapy.Field()    # 口味
    envir = scrapy.Field()    # 环境
    service = scrapy.Field()  # 服务
    company = scrapy.Field()  # 企业名称
    company_address = scrapy.Field() # 企业地址
    company_type = scrapy.Field()    # 主体业态
    company_style = scrapy.Field()   # 经营范围
