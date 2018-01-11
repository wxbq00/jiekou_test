from bs4 import BeautifulSoup
import requests
r = requests.get("http://www.cnblogs.com/yoyoketang/")
content=r.content#获取html内容
soup=BeautifulSoup(content,'html.parser')#解析html
times=soup.find_all(class_='dayTitle')
title=soup.find_all(class_='postTitle')
con=soup.find_all(class_='postCon')
for i,j,k in zip(times,title,con):
    print(i.a.string)
    print(j.a.string)
    print(k.div.contents[0])
