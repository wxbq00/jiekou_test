import requests
import requests.cookies
#cookie
url='https://coding.imooc.com'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

}
s=requests.session()
r=s.get(url,headers=headers)
print(s.cookies)
c=requests.cookies.RequestsCookieJar()
c.set('imooc_uuid','d65724cd-5aee-483a-8b9e-49c5068a112e')
c.set('imooc_isnew_ct','1513499389')
c.set('Hm_lvt_c1c5f01e0fc4d75fd5cbb16f2e713d56','1513499395')
c.set('last_login_username','1823327404%40qq.com')
c.set('imooc_isnew','2')
c.set('Hm_lpvt_c1c5f01e0fc4d75fd5cbb16f2e713d56','1514171539')
c.set('cvde','5a362afd3dde9-31')
s.cookies.update(c)
