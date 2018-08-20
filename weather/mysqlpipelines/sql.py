import pymysql

conn = pymysql.connect(host='119.3.56.137',port=3306,database='yigong_db',user='fangxiaoding',password='Dfkj87658006_Yz',charset='utf8')
cur = conn.cursor()

class Sql:
    @classmethod
    def select_city(cls, city):
        sql = '''select city_id from city where `name` LIKE %(name)s'''
        value = {
            "name": city
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def select_id(cls, city_id):
        sql = '''select id from weather where `city_id`=%(city_id)s'''
        value = {
            "city_id": city_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def replace_name(cls, id,city_id, list_id,  province, date_wea, wea, max, min, win, update_time):
        sql = ''' replace into weather(`id`,`city_id`, `list_id`,  `province`, `date_wea`, `wea`, `max`, `min`, `win`, `update_time`) 
                          values (%(id)s,%(city_id)s,%(list_id)s,%(province)s,%(date_wea)s,%(wea)s,%(max)s, %(min)s,%(win)s,%(update_time)s)'''
        value = {
            "id": id,
            "city_id": city_id,
            "list_id": list_id,
            "province": province,
            "date_wea": date_wea,
            "wea": wea,
            "max": max,
            "min": min,
            "win": win,
            "update_time": update_time,
        }
        cur.execute(sql, value)
        conn.commit()
        print('*'*100)

    @classmethod
    def insert_name(cls, city_id, list_id,  province, date_wea, wea, max, min, win, update_time):
        sql = ''' replace into weather(`city_id`, `list_id`,  `province`, `date_wea`, `wea`, `max`, `min`, `win`, `update_time`) 
                          values (%(city_id)s,%(list_id)s,%(province)s,%(date_wea)s,%(wea)s,%(max)s, %(min)s,%(win)s,%(update_time)s)'''
        value = {
            "city_id": city_id,
            "list_id": list_id,
            "province": province,
            "date_wea": date_wea,
            "wea": wea,
            "max": max,
            "min": min,
            "win": win,
            "update_time": update_time,
        }
        cur.execute(sql, value)
        conn.commit()
        print('#'*100)

def close_spider(spider):
    conn.close()
    cur.close()
    print("Done!!")