# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time
from .sql import Sql
from ..items import WeatherItem

class WeatherPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, WeatherItem):
            city_id = Sql.select_city(item['city'])
            print('这是城市ID:', city_id)
            time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print(time_now)

            if city_id is not None:
                id = Sql.select_id(city_id)
                print(city_id)
                Sql.replace_name(id, city_id, item['list_id'], item['pro'], item['date'], item['wea'], item['max'],item['min'], item['win'], time_now)
                Sql.insert_name(city_id, item['list_id'], item['pro'], item['date'], item['wea'], item['max'],item['min'], item['win'], time_now)










# class WeatherPipeline(object):
#     def open_spider(self, spider):
#         self.connect = pymysql.connect(host='106.14.2 48.127',
#                                        port=3366,
#                                        database='yigong_db',
#                                        user='root',
#                                        password='H3Xhvf9MOGu9h008UzZq',
#                                        charset='utf8'
#             )
#         self.cursor = self.connect.cursor()
#
#     def process_item(self, item, spider):
#         self.cursor.execute(
#             ''' select city_id from city where name LIKE %s ''', item['city']
#         )
#         city_id = self.cursor.fetchone()
#         print('这是城市id:' ,city_id)
#
#         time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#         if city_id is not None:
#             self.cursor.execute(
#                 '''select id from python_weather where city_id=%s''', city_id
#             )
#             id = self.cursor.fetchone()
#
#             self.cursor.execute(
#                 ''' replace into
#                     weather(id,city_id, list_id,  province, date_wea, wea, max, min, win, update_time)
#                     values (%s,%s,%s,%s,%s,%s,%s, %s,%s,%s)''',
#                 (
#                     id,
#                     city_id,
#                     item['list_id'],
#                     item['pro'],
#                     item['date'],
#                     item['wea'],
#                     item['max'],
#                     item['min'],
#                     item['win'],
#                     time_now
#                 )
#             )
#             self.connect.commit()
#             print('*'*100)
#
#             self.cursor.execute(
#                 ''' insert into
#                     weather_backup(city_id, list_id,  province, date_wea, wea, max, min, win, update_time)
#                     values (%s,%s,%s,%s,%s,%s, %s,%s,%s)''',
#                 (
#                     city_id,
#                     item['list_id'],
#                     item['pro'],
#                     item['date'],
#                     item['wea'],
#                     item['max'],
#                     item['min'],
#                     item['win'],
#                     time_now
#                 )
#             )
#             self.connect.commit()
#             print('#'*100)

    # def close_spider(self, spider):
    #     # 关闭
    #     self.cursor.close()
    #
    #     self.connect.close()
    #     # 打印done表示完成
    #     print("done!!!")

