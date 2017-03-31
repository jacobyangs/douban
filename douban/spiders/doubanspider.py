# -*- coding: utf-8 -
from scrapy import Spider
from scrapy.http import FormRequest
from douban.items import DoubanItem
from scrapy.selector import Selector
import time
from datetime import datetime
import json
import hashlib
import re
class Douban(Spider):
    name = 'doubanspider'
    allowed_domains = ['movie.douban.com']
    limit = 50
    page_start = 0
    download_delay = 2
    count = 0
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=治愈&page_limit="+str(limit)+"&page_start="+str(page_start)
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    def start_requests(self):
        yield FormRequest(url=self.url,
                         callback=self.parse_page,meta={'dont_merge_cookies': True},headers=self.headers)
    def parse_page(self,response):
        # print response.body
        datas = json.loads(response.body)["subjects"]
        for data in datas:
            self.count = self.count+1
            item = DoubanItem()
            item["url"] = data["url"]
            item["rate"] = data["rate"]
            item["cover_x"] = data["cover_x"]
            item["is_beetle_subject"] = data["is_beetle_subject"]
            item["title"] = data["title"]
            item["playable"] = data["playable"]
            item['cover'] = data['cover']
            item["cover_y"] = data["cover_y"]
            item["is_new"] = data["is_new"]
            item["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield FormRequest(url=item["url"],callback=self.parse_item,meta={'item': item},headers=self.headers)
            if self.count%50 == 0:
                self.page_start = self.page_start + self.limit
                url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=" + str(
                    self.limit) + "&page_start=" + str(self.page_start)
                yield FormRequest(url=url,callback=self.parse_page,headers=self.headers)



    def parse_item(self,response):
        item = response.meta['item']
        item["actor"] = response.xpath('//span[@class=\'actor\']/span/a/text()').extract() #actor
        item["director"] = Selector(text=response.xpath('//span[@class=\'attrs\']').extract()[0]).xpath("//a/text()").extract()  #daoyan
        item["scriptwriter"] = Selector(text=response.xpath('//span[@class=\'attrs\']').extract()[1]).xpath("//a/text()").extract()  #bianju
        item["type"] = response.xpath('//span[@property=\'v:genre\']/text()').extract()  #leixing
        item["country"] = response.xpath("//div[@id=\'info\']/text()").extract()[8]   #zhipianguojia
        item["language"] = response.xpath("//div[@id=\'info\']/text()").extract()[10]   #yuyang
        item["uptime"] = response.xpath('//span[@property=\'v:initialReleaseDate\']/text()').extract()  #shangyinshijian
        item["hotjudge"] = [x.strip() for x in response.xpath("//p[@class=\'""\']/text()").extract()]      #hot judge
        item["sorce"] = response.xpath("//strong[@property=\"v:average\"]/text()").extract()[0]         #sorce
        item["body"] = response.body
        try:
            item["anthorname"] = response.xpath("//div[@id=\'info\']/text()").extract()[16]  # anthor name
            item["imdblink"] = response.xpath("//div[@id=\'info\']/a[@target=\'_blank\']/@href").extract()[0]  #imdb
            item["summary"] = response.xpath("//span[@property=\'v:summary\']/text()").extract()[0].strip()  # jian jie
        except:
            pass
        return item
    def parse_date(self, input):
        if input is None:
            return None
        else:
            return datetime.now().strptime(input, '%Y-%m-%d %H:%M')

    def json_date(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        else:
            return json.JSONEncoder.default(self, obj)

    def getstr_md5(self, input):
        if input is None:
            input = ''
        md = hashlib.md5()
        md.update(input)
        return md.hexdigest()

    def getTimeStamp(self, data_in):
        if time is None:
            return 0
        try:
            return time.mktime(time.strptime(data_in, '%Y-%m-%d'))
        except:
            return 0

    def getMatch(self, patten, str):
        match = re.search(patten, str)
        if match:
            return match.group()
        else:
            return None

