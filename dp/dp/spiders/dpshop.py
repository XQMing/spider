# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings
from dp.items import DpItem
from scrapy.selector import Selector
import os
os.environ["http_proxy"] = "http://username:password@172.19.194.60:8080"

class DpshopSpider(scrapy.Spider):
    name = 'dpshop'
    allowed_domains = ['dianping.com']
    #meta = {'dont_redirect': True,'allow_redirects':False,'handle_httpstatus_list': [301, 302]}
    cookie = settings['COOKIE']
    print(cookie)
    x = input('please confirm cookie:')
    headers = {
    'Host': 'www.dianping.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Proxy-Connection': 'keep-alive',}
    # foodtype = ['g1783','g34014','g34015','g34032','g34055','g2714','g101','g203','g102','g251','g103','g104','g247','g106','g105',
    #             'g215','g25474','g107','g3243','g26481','g109','g508','g132','g110','g219','g111','g112','g113','g115','g116','g117',
    #             'g248','g118','g4467','g4469','g4473','g205','g206','g207','g1947','g198','g199','g202','g200','g201','g3017','g34060',
    #             'g34061','g34062','g34063','g34064','g34065','g34066','g208','g32733','g32731','g3027','g4477','g3023','g1338','g2774',
    #             'g311','g246','g26484','g26482','g249','g26483','g250','g252','g133','g134','g240','g241','g242','g243','g244','g231',
    #             'g232','g233','g234','g253','g254','g24340','g238','g238','g227','g230','g229','g228','g25151','g33924','g34040','g34041',
    #             'g224','g225','g226','g34044','g210','g211','g1819','g1881','g212','g213','g1821','g214','g216','g217','g220','g223','g222','g221']
    # region = ['r3','r4','r2','r10','r6','r9','r7','r12','r13','r5','r5937','r5938','r5939','r8847','r8846','c3580']

    foodtype = ['g3023']
    region = ['r6']

    def start_requests(self):
        for food in self.foodtype:
            for qu in self.region:
                url = 'http://www.dianping.com/shanghai/ch10/%s%s' % (food,qu)
                yield scrapy.Request(url, callback=self.parse_list,cookies=self.cookie,headers=self.headers)

    def parse_list(self,response):
        selector = Selector(response)
        pg = 0
        pages = selector.xpath('//div[@class="page"]/a/@data-ga-page').extract()

        if len(pages) > 0:
            pg = pages[len(pages) - 2]
        pg = int(str(pg))+1
        url = str(response.url)

        for p in range(1,pg):
            ul = url+'p'+str(p)
            yield scrapy.Request(ul,callback=self.parse,cookies=self.cookie,headers=self.headers)

    def parse(self, response):
        n1 = response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a[1]/@data-shopid').extract()
        n2 = int(len(n1)+1)
        for i in range(1,n2):
            info = DpItem()
            shop_page_href = response.xpath('//*[@id="shop-all-list"]/ul/li'+'['+str(i)+']'+'/'+'div[2]/div[1]/a[1]/@href').extract()[0]
            info['url'] = response.xpath('//*[@id="shop-all-list"]/ul/li'+'['+str(i)+']'+'/'+'div[2]/div[1]/a[1]/@href').extract()[0]
            info['address'] = response.xpath('//*[@id="shop-all-list"]/ul/li'+'['+str(i)+']'+'/'+'div[2]/div[3]/span/text()').extract()[0]
            yield scrapy.Request(shop_page_href, callback=self.parse_next ,dont_filter=True,meta={'items':info},cookies=self.cookie,headers=self.headers)


    def parse_next(self, response):
        info = response.request.meta['items']
        try:
            info['city'] = response.xpath('//*[@id="logo-input"]/div/a[2]/span[2]/text()').extract()[0]
        except IndexError:
            info['city'] = ''
        else:
            info['city'] = response.xpath('//*[@id="logo-input"]/div/a[2]/span[2]/text()').extract()[0]
        info['name'] = response.xpath('//*[@id="body"]/div/div[1]/span/text()').extract()[0]
        try:
            info['district'] = response.xpath('//*[@id="body"]/div/div[1]/a[3]/text()').extract()[0]
        except IndexError:
            info['district'] = ''
        else:
            info['district'] = response.xpath('//*[@id="body"]/div/div[1]/a[3]/text()').extract()[0]
        try:
            info['plate'] = response.xpath('//*[@id="body"]/div/div[1]/a[4]/text()').extract()[0]
        except IndexError:
            info['plate'] = ''
        else:
            info['plate'] = response.xpath('//*[@id="body"]/div/div[1]/a[4]/text()').extract()[0]
        info['type'] = response.xpath('//*[@id="body"]/div/div[1]/a[2]/text()').extract()[0]
        info['comment_number'] = response.xpath('//*[@id="reviewCount"]/text()').extract()[0]
        info['comsume'] = response.xpath('//*[@id="avgPriceTitle"]/text()').extract()[0]
        info['taste'] = response.xpath('//*[@id="comment_score"]/span[1]/text()').extract()[0]
        info['envir'] = response.xpath('//*[@id="comment_score"]/span[2]/text()').extract()[0]
        info['service'] = response.xpath('//*[@id="comment_score"]/span[3]/text()').extract()[0]
        try:
            info['classify'] = response.xpath('//*[@id="cate-channel"]/div[1]/div/span/text()').extract()[0]
        except IndexError:
            info['classify'] = ''
        else:
            info['classify'] = response.xpath('//*[@id="cate-channel"]/div[1]/div/span/text()').extract()[0]

        try:
            info['company'] = response.xpath('//*[@id="shop-tabs"]/div[@class="shop-food-safety clearfix J-panel Hide"]/ul/li[2]/text()').extract()[0]
        except IndexError:
            info['company'] = ''
        else:
            info['company'] = response.xpath('//*[@id="shop-tabs"]/div[@class="shop-food-safety clearfix J-panel Hide"]/ul/li[2]/text()').extract()[0]

        try:
            info['company_address'] = response.xpath('//*[@id="shop-tabs"]/div[@class="shop-food-safety clearfix J-panel Hide"]/ul/li[4]/text()').extract()[0]
        except IndexError:
            info['company_address'] = ''
        else:
            info['company_address'] = response.xpath('//*[@id="shop-tabs"]/div[@class="shop-food-safety clearfix J-panel Hide"]/ul/li[4]/text()').extract()[0]

        try:
            info['company_type'] = response.xpath('//*[@id="shop-tabs"]/div[@class="shop-food-safety clearfix J-panel Hide"]/ul/li[5]/text()').extract()[0]
        except IndexError:
            info['company_type'] = ''
        else:
            info['company_type'] = response.xpath('//*[@id="shop-tabs"]/div[@class="shop-food-safety clearfix J-panel Hide"]/ul/li[5]/text()').extract()[0]

        try:
            info['company_style'] = response.xpath('//*[@id="shop-tabs"]/div[@class="shop-food-safety clearfix J-panel Hide"]/ul/li[6]/text()').extract()[0]
        except IndexError:
            info['company_style'] = ''
        else:
            info['company_style'] = response.xpath('//*[@id="shop-tabs"]/div[@class="shop-food-safety clearfix J-panel Hide"]/ul/li[6]/text()').extract()[0]


        yield info
