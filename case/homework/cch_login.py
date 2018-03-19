import requests
url='https://stagingcachecache.cache-cache.cn/api/users/login'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

}
payload={"email":"admin@example.com","password":"password","remember":True}
r=requests.get(url,headers=headers,data=payload)
print(r.content)