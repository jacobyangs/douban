# -*- coding: utf-8 -*-
import re
from scrapy.conf import settings
class RedisCollection(object):
    def __init__(self,OneUrl):
        self.collectionname = OneUrl
    def getCollectionName(self):
        if self.IndexAllUrls() is not None:
            name = self.IndexAllUrls()
        else:
            name = 'publicurls'
        return name
    def IndexAllUrls(self):
        allurls = ["douban"]
        result = None
        for str in allurls:
            if re.findall(str,self.collectionname):
                result = str
                break
        return result
