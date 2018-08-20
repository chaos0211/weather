# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import copy
import re
from ..items import WeatherItem
from bs4 import BeautifulSoup
import datetime
import time


class TianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['weather.com.cn']
    # start_urls = ['http://www.weather.com.cn/weather1d/101010100.shtml']
    start_urls = ['http://www.weather.com.cn/weather1d/{}.shtml']

    def start_requests(self):
        a = requests.get("http://mobile.weather.com.cn/js/citylist.xml").content
        b = etree.HTML(a)
        item = WeatherItem()
        c = b.xpath("//d")
        for d in c:
            item['list_id'] = d.xpath('./@d1')
            # print(type(item['id']))
            item['list_id'] = ''.join(item['list_id'])
            item['city'] = d.xpath('./@d2')
            item['city'] = ''.join(item['city']) + '%'
            item['pro'] = d.xpath('./@d4')
            if int(item['list_id']) < 102170101:

                yield scrapy.Request(
                    url=self.start_urls[0].format(item['list_id']),
                    callback=self.parse,
                    meta={'item':copy.deepcopy(item)}
                )

    def parse(self, response):
        item = response.meta['item']
        # item = WeatherItem()
        item['date'] = str(datetime.datetime.now().month) + '月' + str(datetime.datetime.now().day) + '日'
        item['wea'] = response.xpath("//p[@class='wea']/text()").extract_first()
        item['max'] = response.xpath("//p[@class='tem']/span/text()").extract()[0]
        item['min'] = response.xpath("//p[@class='tem']/span/text()").extract()[1]
        item['win'] = response.xpath("//p[@class='win']/span/text()").extract_first()
        print(item)
        yield item


    # def parse(self, response):
    #     item = response.meta['item']
    #     # item = WeatherItem()
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #
    #     # 分析得 <ul class="t clearfix"> 标签下记录了我们想要的数据,因此只需要解析这个标签即可
    #     ul_tag = soup.find('ul', 't clearfix')  # 利用 css 查找
    #     # print(ul_tag) # 取出七天数据
    #
    #     # 打印每一天数据
    #     li_tag = ul_tag.findAll('li')
    #     for tag in li_tag:
    #         # d_mon = datetime.date.today().month
    #         # print(tag.find('h1').string)   # 时间
    #         item['date'] = tag.find('h1').string
    #         item['date'] = re.findall(r'\d+\.?\d*', item['date'])[0]
    #         item['date'] = str(datetime.date.today().month) + '月' + item['date'] + '日'
    #         # print(tag.find('p', 'wea').string)
    #         item['wea'] = tag.find('p', 'wea').string
    #         # 温度的tag格式不统一,做容错
    #         try:
    #             # print(tag.find('p', 'tem').find('span').string)  # 高温
    #             item['max'] = tag.find('p', 'tem').find('span').string
    #             # print(tag.find('p', 'tem').find('i').string)     # 低温
    #             item['min'] = tag.find('p', 'tem').find('i').string
    #         except:
    #             print('没有高温或低温数据')
    #             pass
    #         # print(tag.find('p', 'win').find('i').string)  # win
    #         item['win'] = tag.find('p', 'win').find('i').string
    #         # print("_______________ 分割线 ____________________")
    #         print(item)
    #         yield item
    #         print(type(item))
