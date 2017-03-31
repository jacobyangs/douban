# -*- coding: utf-8 -

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.item import DictItem, Field
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime
import hashlib
import re
import json
import time
import scrapy
from scrapy.selector import Selector
from scrapy.conf import settings
from elasticsearch import Elasticsearch
if __name__ == '__main__':
    client = Elasticsearch("localhost")
    print client.cluster.stats()

