# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings
from dp.items import DpItem
import json

class DpshopSpider(scrapy.Spider):
    name = 'dpshop'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/shanghai/ch10/g110p%s' % p for p in range(1, 2)]
    # meta = {
    #     'dont_redirect': True,  # 禁止网页重定向
    #     'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    # }
    #cookie = settings['COOKIE']
    # def start_requests(self): # 重构start_requests方法
    #     yield scrapy.Request(self.start_urls[0],callback=self.parse,cookies=self.cookie)
    #https://github.com/ppy2790/dianpingshop/tree/master/dianpingshop
    #https://github.com/Liangchengdeye/DaZhongdianping
    def parse(self, response):
        # shop_page = '//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a[1]'
        # address_info = '//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/span'
        for i in range(1,16):  #response.xpath('//*[@id="shop-all-list"]/ul/li'):
            info = DpItem()
            shop_page_href = response.xpath('//*[@id="shop-all-list"]/ul/li'+'['+str(i)+']'+'/'+'div[2]/div[1]/a[1]/@href').extract()[0]
            info['url'] = response.xpath('//*[@id="shop-all-list"]/ul/li'+'['+str(i)+']'+'/'+'div[2]/div[1]/a[1]/@href').extract()[0]    #/div[2]/div[1]/a[1]
            info['address'] = response.xpath('//*[@id="shop-all-list"]/ul/li'+'['+str(i)+']'+'/'+'div[2]/div[3]/span/text()').extract()[0] #//*[@id="shop-all-list"]/ul/li[1]/div[2]/div[3]/span
            yield scrapy.Request(shop_page_href, callback=self.parse_next ,dont_filter=True ,meta={'items':info})

    def parse_next(self, response):
        info = response.request.meta['items']
        info['name'] = response.xpath('//*[@id="body"]/div/div[1]/span/text()').extract()[0]
        info['district'] = response.xpath('//*[@id="body"]/div/div[1]/a[3]/text()').extract()[0]
        info['plate'] = response.xpath('//*[@id="body"]/div/div[1]/a[4]/text()').extract()[0]
        info['type'] = response.xpath('//*[@id="body"]/div/div[1]/a[2]/text()').extract()[0]
        info['comsume'] = response.xpath('//*[@id="avgPriceTitle"]/text()').extract()[0]
        info['taste'] = response.xpath('//*[@id="comment_score"]/span[1]/text()').extract()[0]
        info['envir'] = response.xpath('//*[@id="comment_score"]/span[2]/text()').extract()[0]
        info['service'] = response.xpath('//*[@id="comment_score"]/span[3]/text()').extract()[0]
        info['classify'] = response.xpath('//*[@id="cate-channel"]/div[1]/div/span/text()').extract()[0]
        if response.xpath('//*[@id="shop-tabs"]/div[6]/ul/li[2]/text()') == '':
            info['company'] = response.xpath('//*[@id="shop-tabs"]/div[6]/ul/li[2]/text()').extract()[0]
        else:
            info['company'] = ''
        if response.xpath('//*[@id="shop-tabs"]/div[6]/ul/li[4]/text()') == '':
            info['company_address'] = response.xpath('//*[@id="shop-tabs"]/div[6]/ul/li[4]/text()').extract()[0]
        else:
            info['company_address'] = ''
        if response.xpath('//*[@id="shop-tabs"]/div[6]/ul/li[6]/text()') == '':
            info['company_style'] = response.xpath('//*[@id="shop-tabs"]/div[6]/ul/li[6]/text()').extract()[0]
        else:
            info['company_style'] = ''
        yield info


    # def parse(self, response):
    #     shop_page = '//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a[1]'
    #     for page in response.xpath(shop_page):
    #         shop_page_href = page.xpath('@href').extract()[0]
    #         yield scrapy.Request(shop_page_href, callback=self.parse_next, dont_filter=True)
    #
    # def parse_next(self, response):
    #     info = DpItem()
    #     info['name'] = response.xpath('//*[@id="basic-info"]/h1/text()').extract()[0]
    #     info['district'] = response.xpath('//*[@id="body"]/div/div[1]/a[3]/text()').extract()[0]
    #     info['plate'] = response.xpath('//*[@id="body"]/div/div[1]/a[4]/text()').extract()[0]
    #     info['type'] = response.xpath('//*[@id="body"]/div/div[1]/a[2]/text()').extract()[0]
    #     info['address'] = response.xpath('//*[@id="address"]').extract()[0]
    #     yield info

    # def parse_next_page(self, response):
    #     info = response.request.meta['items']
    #     address_info = '//*[@id="shop-all-list"]/ul/li/div[2]/div[3]'
    #     for pg in response.xpath(address_info):
    #         info['address'] = pg.xpath('span/text()').extract()[0]
    #         yield info



