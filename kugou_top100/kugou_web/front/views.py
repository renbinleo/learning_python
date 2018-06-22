from django.shortcuts import render
import pymysql


def get_data(sql):#获取数据库的数据
    conn = pymysql.connect(host="localhost", user="kugou", password="password", db="kugou", use_unicode=True, charset="utf8mb4")
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall() # 搜取所有结果
    cur.close()
    conn.close()
    return results
def order(request):# 向页面输出订单
    sql = "SELECT * FROM `kugou`   LIMIT 100"
    m_data = get_data(sql)
    return render(request,'order_list.html',{'order':m_data})