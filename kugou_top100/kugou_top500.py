#coding=utf-8

import requests
from bs4 import BeautifulSoup
from kugou_mysql import to_mysql

headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}

def get_info(url):

    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    paimings = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    shichangs = soup.select('span.pc_temp_tips_r > span')
    for paiming,title,shichang in zip(paimings,titles,shichangs):
        rank = paiming.get_text().strip()
        song = title.get_text().strip().split('-')[1]
        singer = title.get_text().strip().split('-')[0]
        tryurl = title.get('href')
        duration = shichang.get_text().strip()
        to_mysql(int(rank),song,singer,tryurl,duration)
        data={
            '排名':rank,
            '歌名':song,
            '歌手': singer,
            '试听URL':tryurl,
            '时长':duration
        }
        print(data)

if __name__=='__main__':
# get_info('http://www.kugou.com/yy/rank/home/1-8888.html')
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1,21)]

for url in urls:

    get_info(url)