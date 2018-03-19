import requests
import requests.cookies
url='https://passport.cnblogs.com/user/signin'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
,
}
r=requests.get(url,headers=headers)
c=requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie','7FDD0BE3AEE4CB1EEA3D3D3859773F24F0677EAE07A7DEB93EB9959CCDC6A299E8157DCF51F7C6AE556B5A0BAA5C50855F637D8DE99A0A41CC7B247CAD9CBAC9BE0B6033C8776CEC24E532515489065706B30FD0')
c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8Gf3jjv4cttDnEy2UYRcGZ36UdTJkDaT31pAmvK6klEgHDMYDYby7nJgH_HYL76pZyS1AjkST7tWy_1IWQUMP0IaltfNeTUZGz__mmsSZy2xn8nYFvDrbhuWHmJvTRUaW6bEjmKZfneRDnsrvzaDgwwxeOt0g9eWd6zjpCRQJYqx9Eko4VEK_xcBVtkE54LvWGRQbtohwDGjBthNnpWsGWyKWZ24hJjaUR4ShFl0XFr5EUjCfK1Xs1z1xHqlyOaZyVuhz_nTQlUCDC3JI_tojftX72RWzfJTdu6FHULkeP1X')
c.set('AlwaysCreateItemsAsActive',"True")
c.set('AdminCookieAlwaysExpandAdvanced',"True")
r.cookies.update(c)
print(r.cookies)

payload={"input1":"RVvfWuSpylJvYET/aGwkDkMWloZ38I2y3SHDUJ/GHVT07nXXlPc6w/Gfs4W+Jt8B7q+4e/TJKwFC7bzCdxzW7PK8vHdFLlQ5xrm7NCNugKAs5LOG91BEtut3mLUuW4x4wKaVWHoQ7/92BYQtGYexf1V1jC9TxxVWMk+q4kCl45k=","input2":"x5OBACFTgucMVsSj5eTs//kVRz6CcMGET1jl16SmFVd74AIOC2D+AsiigzMi9yc8wnXHZKU5VtQhwfvQ6w1J97MKUfcI5FgvJVXnkiw1jKcrDLoOxincj9tgNGV9+2TardI+es/ZwFsQ+yxvibzPPGaaJEroxGzyQC7l6SBPmKg=","remember":False,"geetest_challenge":"f4cce47f9c2445bd2e2fb0e5fa1910ea","geetest_validate":"e156b79718e5aee5ac32db438e026fa2","geetest_seccode":"e156b79718e5aee5ac32db438e026fa2|jordan"}
s=requests.session()
#先登录
r1=s.post(url,json=payload,headers=headers)

url2='https://i.cnblogs.com/EditPosts.aspx?opt=1'
body={'Editor$Edit$txbTitle':'test3',
      'Editor$Edit$EditorBody':'<p>xxx</p>',
      'Editor$Edit$lkbPost':'发布'}
r=requests.get(url2,data=body)
print(r.content)


