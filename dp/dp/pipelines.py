# -*- coding: utf-8 -*-
# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DpPipeline(object):
    def process_item(self, item, spider):
        item['district'] = item['district'].replace(' ', '')
        item['envir'] = item['envir'].replace('环境:', '')
        if item['envir'] == '-':
            item['envir'] = ''
        item['taste'] = item['taste'].replace('口味:', '')
        if item['taste'] == '-':
            item['taste'] = ''
        item['service'] = item['service'].replace('服务:', '')
        if item['service'] == '-':
            item['service'] = ''
        item['comsume'] = item['comsume'].replace('人均:', '').replace('元','')
        if item['comsume'] == '-':
            item['comsume'] = ''
        item['classify'] = item['classify'].replace('全部', '').replace('分类', '')
        item['comment_number'] = item['comment_number'].replace('条评论', '')
        if item['comment_number'] == '0':
            item['comment_number'] = ''
        return item
