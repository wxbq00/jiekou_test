# coding:utf-8
import unittest
import requests
from common.logger import Log
# 禁用安全请求警告
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Blog_login(unittest.TestCase):
    log = Log()
    def login(self, username, psw, reme=True):
        '''三个参数：
        账号：username，密码：psw,记住登录：reme=True'''
        url = "https://passport.cnblogs.com/user/signin"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
            "Cookie": "_ga=GA1.2.382458561.1513424506; ASP.NET_SessionId=rnzzmuevfbq0iwrr1c5kqree; SERVERID=fc59f0882c6e4b75dcaad92e7e90772e|1515641166|1515641165",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Content-Length": "554"
                 }
        json_data = {"input1": username,
                "input2": psw,
                "remember": reme}


        res = requests.post(url, headers=header, json=json_data, verify=False)
        result1 = res.content  # 字节输出
        self.log.info("博客园登录结果：%s"%result1)
        return res.json()      # 返回json

    def test_login1(self):
        u'''测试登录：正确账号，正确密码'''
        self.log.info("------登录成功用例：start!---------")
        username = "lO7tIEbw4BFPuh5IjgMT+9NibZeGt0sj7M3AWdLNTofze6yPrxVJLZEkmQL2XPwV9bngoqu7CSCs/fxukLr2XzLmgz9dta2caDdQIsxlyOg2CRNFuxUYvU5Fk7VGSf1breJfz1SD1uX/kbYFLB0AB++Xr/7sHTsuWZ0Fhz7vYys=",#这里是抓包后获取的博客园的加密账号
        self.log.info("输入正确账号：%s"%username)
        psw = "MphGAsMExHYs7k4dXgQKzKSl2Pou/MRfKRVEMaqjgaFmXDAzMtit4uUZSqEzFv4CEynLTSgrFhv7sc6K+PHUEOWucGKx/AgOYBO5fW4sYiU470BRRbJuYlIqZQjRq4UJf37jjjOVpiLYQV0K45BSH6jk370Z0e/cG5skWRIh380=",#这里是抓包后获取的博客园的加密密码
        self.log.info("输入正确密码：%s"%psw )
        result = self.login(username, psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result["success"], True)
        self.log.info("------pass!---------")

    def test_login2(self):
        u'''测试登录：正确账号，错误密码'''
        self.log.info("------登录失败用例：start!---------")
        username = "这里是抓包后获取的博客园的加密账号",
        self.log.info("输入正确账号：%s"%username)
        psw = "xxx",
        self.log.info("输入错误密码：%s"%username)
        result = self.login(username, psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result["success"], False)
        self.log.info("------pass!---------")


if __name__ == "__main__":
    unittest.main()
