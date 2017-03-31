# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,codecs
from elasticsearch import Elasticsearch
from douban.redisoper import RedisOpera
from scrapy.conf import settings

class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item
class JSONPipeline(object):
    def __init__(self):
        self.file = codecs.open('demo_out.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=True) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
class InsertElastic(object):
    def __init__(self):
        self.es = Elasticsearch(settings["ELASTICHOST"])
    def process_item(self,item,spider):
        self.es.create(settings['ELASTICINDEX'],settings["ELASTICTYPE"],body= json.dumps(item, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        return item
class InsertRedis(object):
    def __init__(self):
        self.Redis = RedisOpera('insert')
    def process_item(self,item,spider):
        self.Redis.write(item['url'])
        return item