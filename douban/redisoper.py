# -*- coding: utf-8 -*-
import redis
from scrapy import log
from douban.util import RedisCollection
from scrapy.conf import settings
class RedisOpera:
    def __init__(self,stat):
        log.msg('init redis %s connection!!!!!!!!!!!!!!!!!!!!!!!!!' %stat,log.INFO)
        self.r = redis.Redis(host=settings["REDIS_SERVER"],port=settings["REDIS_PORT"],db=settings["REDIS_DB"])

    def write(self,values):
        # print self.r.keys('*')
        collectionname = RedisCollection(values).getCollectionName()
        self.r.sadd(collectionname,values)
    def query(self,values):
        collectionname = RedisCollection(values).getCollectionName()
        return self.r.sismember(collectionname,values)
