import requests
class blog():
    def __init__(self,s):
        self.s=s
    def login(self):
        url = 'https://passport.cnblogs.com/user/signin'
        headers={
        'Cookie': '__utma=226521935.941366269.1508751496.1508751496.1508751496.1; __utmz=226521935.1508751496.1.1.utmccn=(organic)|utmcsr=baidu|utmctr=|utmcmd=organic; __gads=ID=8019f9e6f4ec84a4:T=1509541344:S=ALNI_MaHsxheE6Nqp15k7DfgUGc45I0SMQ; UM_distinctid=15f80eaa2b73fe-03faa50a5ce9df-193e6d56-fa000-15f80eaa2b83d6; CNZZDATA1258637387=1850015044-1509693391-null%7C1509693391; CNZZDATA3347352=cnzz_eid%3D1352186815-1509957096-null%26ntime%3D1510903373; _ga=GA1.2.479464532.1501746521; _gid=GA1.2.1459045168.1515377290'
      ,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        ,"Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "557",

        "Connection": "keep-alive",
        'Accept':'application / json, text / javascript, * / *; q = 0.01'

    }
        payload = {
            'input1': 'gbNFGhVhXxIH5+JMoeKPBusQiFmS2fTt5qm2Y+VTMkHUNtHkS9eKbZUwiR3J3zEBDADBvzCRuIXxnuhVkz97Gd92cec5jZYUNedYiVdYMPK4ULB3WhCxtHmtkKLDfg3xP2LcjrsK8u2vIZ3kETjVES3EwaxviNn+qWTAwRLJ5zQ='
            ,
            'input2': 'VDNPL53eINNwunQHa13D0lNmVYEzyZ8o/RmyuHG5lhPG/QMVaRMFNvX/mxbt27b1Fygi73NyNZZYIrL8+vp0+X3dsZro/0kXSkAfOUiwVRUv5y6WVAC3SmbLk/WqpJbR+WyV7GZWCCERSgnoDlUSaCK7brhcE7gV5OMVCufrZ+Y='
            , 'remember': 'false',
            'geetest_challenge':'647143d6449c1a0adf457bf8830e33e0ki',
            'geetest_validate':'5c90b3889408e90f28828c2f78f5778c',
            'geetest_seccode':'5c90b3889408e90f28828c2f78f5778c | jordan',
        }
        r=self.s.post(url,json=payload,headers=headers)
        result=r.content
        print(result)
        print(r.json())
    def save_box(self, title, body_data):
        url2 = 'https://i.cnblogs.com/EditPosts.aspx?opt=1'
        '''# 获取报存之后url地址'''
        body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "FE27D343",
        "Editor$Edit$txbTitle": title,
        "Editor$Edit$EditorBody": "<p>%s</p>"%body_data,
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$Advanced$chkDisplayHomePage": "on",
        "Editor$Edit$Advanced$chkComments": "on",
        "Editor$Edit$Advanced$chkMainSyndication": "on",
        "Editor$Edit$lkbDraft": "存为草稿",
            }
        r2=self.s.post(url2,data=body)
        return r2.url

    def get_postid(self,url):
        '''正则提取postid'''
        import re
        postid = re.findall(r"postid=(.+?)&", url)
        print(postid)# 这里是list
        if len(postid) < 1:
            return ''
        else:
            return postid[0]
if __name__ == '__main__':


        s=requests.session()
        blog(s).login()#验证码缓存已失效
