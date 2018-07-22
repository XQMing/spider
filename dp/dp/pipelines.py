# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DpPipeline(object):
    def process_item(self, item, spider):
        item['envir'] = item['envir'].replace('环境:', '')
        item['taste'] = item['taste'].replace('口味:', '')
        item['service'] = item['service'].replace('服务:', '')
        item['comsume'] = item['comsume'].replace('人均:', '').replace('元','')
        item['classify'] = item['classify'].replace('全部', '').replace('分类', '')
        return item
