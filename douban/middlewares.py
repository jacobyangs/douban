# -*- coding: utf-8 -*-
import random
from scrapy.exceptions import IgnoreRequest
from douban.redisoper import RedisOpera



# class scrapy.downloadermiddlewares.DownloaderMiddleware
class PrintUrlMiddleware(object):
    """ 从下载器处开始拦截/过滤URL """
    def __init__(self):
        print 'execute flite url calss (middleware)'
        # self.Redis = RedisOpera()

    def process_response(self, request, response, spider):
        print request.url +'-----------request'
        # print response.url+'------------response'
        # if self.Redis.query(response.url):
        #     raise IgnoreRequest("IgnoreRequest : %s" % response.url)
        # else:
        #     # Redis.set('url:%s' % response.url, 1)
        return response
class IngoreRequestMiddleware(object):
    def __init__(self):
        self.Redis = RedisOpera('query')
    def process_request(self,request,spider):
        if self.Redis.query(request.url):
            raise IgnoreRequest("IgnoreRequest : %s" % request.url)
        else:
            return None
