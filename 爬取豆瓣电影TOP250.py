"""
爬取豆瓣TOP250明细
此代码只能爬取第一页25条记录
"""

import requests
from bs4 import BeautifulSoup
# 模拟浏览器请求
headers = {
    # 防盗链 告诉服务器请求连接地址从哪里跳过来
    "Referer":"http://movie.douban.com/top250",
    # 用户代理 浏览器基本身份信息
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/114.0.5735.289 Safari/537.36"
}

url = 'https://movie.douban.com/top250'
# 发送请求
response = requests.get(url=url,headers=headers)

soup = BeautifulSoup(response.text,'html.parser')
# print(soup)
all_title = soup.find_all(class_="item")
print(all_title)
count = 0
print('----------------------豆瓣电影-TOP250-----------------------------')
for i in all_title:
    title = i.find('span').text.strip()     # 搜索片名
    point = i.find(class_='rating_num').text.strip()     # 搜索评分
    count += 1
    print('第'+str(count)+'名：片名-《'+title+'》'+'/评分：'+point)