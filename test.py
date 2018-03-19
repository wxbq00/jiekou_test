import requests.cookies
import re
url='https://coding.imooc.com/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

}
d={

    'username':'13166427863',
    'password':'mmjusXy0B67Nsh7Y7wxi0PLQ5wk7GGGU0iVrqXZUkn0sDEzQ0ZcYIEOG3Y3gX4eDCxf7HJAqFLcyRnYksro8ACQB9Vx5%2Fkj39primE3lLDty2%2BskKId1Hw8l1Qse%2F%2FawA9CZiTNToGE7v1p7D%2FUy9vdDXyDFxmkFkgeHJF7LnBo%3D',

    'verify':'',
    'remember':'1',
    'pwencode':'1',
    'browser_key':'38e3d6fccb087e472e5ede594d02bf8b',
    'referer':'https://coding.imooc.com'
}
s=requests.session()#会话
r=s.post(url,headers=headers,data=d)#传data参数
# t=re.findall(r'<b>(.+?)</b>',r.content.decode())
# print(t[0])
# print(t[1])
print(r.content.decode())#要解码
print(s.cookies)
c=requests.cookies.RequestsCookieJar()


