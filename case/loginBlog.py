# coding:utf-8
import requests
from common.logger import Log
# 禁用安全请求警告
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Blog():
    # s = requests.session()  # 全局参数
    log = Log()
    def __init__(self, s):
        self.s = s

    def login(self):
        url = "https://passport.cnblogs.com/user/signin"
        headers = {
            'Cookie': '__utma=226521935.941366269.1508751496.1508751496.1508751496.1; __utmz=226521935.1508751496.1.1.utmccn=(organic)|utmcsr=baidu|utmctr=|utmcmd=organic; __gads=ID=8019f9e6f4ec84a4:T=1509541344:S=ALNI_MaHsxheE6Nqp15k7DfgUGc45I0SMQ; UM_distinctid=15f80eaa2b73fe-03faa50a5ce9df-193e6d56-fa000-15f80eaa2b83d6; CNZZDATA1258637387=1850015044-1509693391-null%7C1509693391; CNZZDATA3347352=cnzz_eid%3D1352186815-1509957096-null%26ntime%3D1510903373; _ga=GA1.2.479464532.1501746521; _gid=GA1.2.1459045168.1515377290'
            ,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
            , "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": "555",

            "Connection": "keep-alive",
            'Accept': 'application / json, text / javascript, * / *; q = 0.01'

        }
        json_data = { 'input1':'gbNFGhVhXxIH5+JMoeKPBusQiFmS2fTt5qm2Y+VTMkHUNtHkS9eKbZUwiR3J3zEBDADBvzCRuIXxnuhVkz97Gd92cec5jZYUNedYiVdYMPK4ULB3WhCxtHmtkKLDfg3xP2LcjrsK8u2vIZ3kETjVES3EwaxviNn+qWTAwRLJ5zQ='
    ,'input2':'VDNPL53eINNwunQHa13D0lNmVYEzyZ8o/RmyuHG5lhPG/QMVaRMFNvX/mxbt27b1Fygi73NyNZZYIrL8+vp0+X3dsZro/0kXSkAfOUiwVRUv5y6WVAC3SmbLk/WqpJbR+WyV7GZWCCERSgnoDlUSaCK7brhcE7gV5OMVCufrZ+Y='
    ,'remember':'false'}


        res = self.s.post(url, headers=headers, json=json_data, verify=False)
        result1 = res.content  # 字节输出
        self.log.info(u"调用登录方法，获取结果：%s"%result1)
        return res.json()

    def save(self, title, body):
        url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
        d = {"__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR":"FE27D343",
            "Editor$Edit$txbTitle":title,
            "Editor$Edit$EditorBody":"<p>%s</p>"%body,
            "Editor$Edit$Advanced$ckbPublished":"on",
            "Editor$Edit$Advanced$chkDisplayHomePage":"on",
            "Editor$Edit$Advanced$chkComments":"on",
            "Editor$Edit$Advanced$chkMainSyndication":"on",
            "Editor$Edit$lkbDraft":"存为草稿",
             }
        r2 = self.s.post(url2, data=d, verify=False)  #保存草稿箱
        self.log.info(u"调用保存草稿箱方法，获取结果：%s"%r2)
        return r2.url

    def get_postid(self, r2_url):
        # 正则表达式提取
        import re
        postid = re.findall(r"postid=(.+?)&", r2_url)  # 这里是list []
        self.log.info(u"正则提取postid，获取结果：%s"%postid)
        return postid[0]

    # def del_tie(self, postid):
    #     del_json = {"postId": postid}
    #     del_url = "https://i.cnblogs.com/post/delete"
    #     r3 = self.s.post(del_url, json=del_json, verify=False)
    #     self.log.info(u"删除草稿箱，获取结果：%s"%r3.json()["isSuccess"])
    #     return r3.json()

if __name__ == "__main__":
    import requests
    s = requests.session()
    Blog(s).login() 