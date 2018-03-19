import requests.cookies
import requests

import urllib3
urllib3.disable_warnings()
# 先打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
}# get方法其它加个ser-Agent就可以了
s = requests.session()
print (s.cookies)
r = s.get(url, headers=headers,verify=False)

c = requests.cookies.RequestsCookieJar()
c.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8N7AeFYNSk1Put6Iydpme2YxuH2pXRv-pR0rSDXnlPeKa_EsZcRSAah2lU4ribolk5Y9xqTXilPMf3u7jctaETdn4mbO1bAKMQeRLHv-XSA7KLDjskJwXhEi6crN_fp_ZWQ9HKFQl8A35F5srN_ua6LWHDMNkwMciqBOBcLCun3Ojyoq9vHZ29Algut83K9MXoZ5BqrbP9vIjptkeitrcWuvjvmH0yX7xCGhv3oQhG3blvf31vsKLtQTdGzqVXBV7jP2FJbqgRvMCep7sqP5NgldPmzPpVp-vYnKdvs6OO-68iGQhgEMld_5p2w_3AZs0w')# 填上面抓包内容
c.set('.CNBlogsCookie','85E56727C5B8865F5128610657C086506B2F06AD9BB901BC4CC656A2BFAC87380AFC4585EE00D32F694F8D8701E2DF7212CB361D6E770668CF6ECEE881DE85CB885528A5A611403A9E482884AEAD37CA0C439FB0')# 填上面抓包内容
#登陆后的cookie
c.set('AlwaysCreateItemsAsActive',"True")
c.set('AdminCookieAlwaysExpandAdvanced',"True")


s.cookies.update(c)
print (s.cookies)
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)
# 保存草稿箱
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
"__VIEWSTATEGENERATOR":"FE27D343",
"Editor$Edit$txbTitle":"xxasd",
        "Editor$Edit$EditorBody":"<p>qweqweqw</p>",
"Editor$Edit$Advanced$ckbPublished":"on",
"Editor$Edit$Advanced$chkDisplayHomePage":"on",
"Editor$Edit$Advanced$chkComments":"on",
"Editor$Edit$Advanced$chkMainSyndication":"on",
"Editor$Edit$Advanced$txbEntryName":"",
"Editor$Edit$Advanced$txbExcerpt":"",
"Editor$Edit$Advanced$tbEnryPassword":"",
"Editor$Edit$lkbDraft":"存为草稿",
}
r2 = s.post(url2, data=body, verify=False)
print (r.content)




