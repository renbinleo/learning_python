# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
def to_mysql(rank,song='',singer='',tryurl='',duration=''):

    conn = pymysql.connect(host="localhost",user="kugou",password="password",db="kugou",use_unicode=True, charset="utf8mb4" )

    # 使用 execute()  方法执行 SQL 查询
    #cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    #data = cursor.fetchone()

    #print("Database version : %s " % data)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    insert = "insert into kugou(排名,歌名,歌手,试听URL,时长) values(%s,%s,%s,%s,%s)"

    try:
        cursor.execute(insert,(rank,song,singer,tryurl,duration))

        conn.commit()
#    except Exception as e:
        #错误回滚
#        db.rollback()
    finally:
    # 关闭数据库连接
        conn.close()

if __name__ == '__main__':
    to_mysql(10)