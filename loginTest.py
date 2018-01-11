# coding:utf-8
import unittest
import requests
class Blog_login(unittest.TestCase):
    def login(self, username, psw, reme=True):
        url='https://www.imooc.com/passport/user/login'
        headers={
            'Cookie': 'imooc_uuid = d65724cd - 5aee - 483a - 8b9e - 49c5068a112e;imooc_isnew_ct = 1513499389;last_login_username = 1823327404 % 40qq.com;imooc_isnew = 2;PHPSESSID = lqikkuimjohgh0drcsppuf9kq3;Hm_lvt_f0cfcccd7b1393990c78efdeebff3968 = 1514172861, 1514462341;IMCDNS = 0;Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968 = 1514886677;cvde = 5a44dc82ab2da - 23'
            ,
            'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 63.0.3239.108Safari / 537.36'
            ,'Connection':' keep - alive',
            'Content - Length': '321',
            'X - Requested - With': 'XMLHttpRequest'

        }
        json_data={
            'input1':username,
            'input2':psw,
            'remember':reme
        }
        res=requests.post(url,headers=headers,json=json_data)
        print(res.content)
        print(res.json)
    def test_login1(self):
        username='13166427863',
        psw='P7rRTZGq7gPDxBwi5GPPoGrxeMNctjx5PMOOu/Q78287T6zSiZra7YS9rYBijMc0/2t7d23mPPu5mQZaMU0ywjAstNL72FaY34qLTeeyGE5sV3KPixKFZe5qdCl2dPXmOBh/j6KWQee26H1moyht3siQCmlvw4TjhHcBl5uZnCc=',
        result=self.login(username,psw)
        self.assertEqual(result['success'],True)
    def test_login2(self):
        username = '13166427863',
        psw='xxx'
        result = self.login(username, psw)
        self.assertEqual(result['success'], True)

if __name__ == '__main__':
    unittest.main()