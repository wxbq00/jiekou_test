# coding:utf-8
import unittest
import requests
class Blog_login(unittest.TestCase):
    def login(self, username, psw, reme=True):
        url='https://www.imooc.com/passport/user/login'
        headers={

            'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 63.0.3239.108Safari / 537.36'
            ,'Connection':' keep - alive',
            'Content - Length': '321',
            'X - Requested - With': 'XMLHttpRequest'

        }
        cookies = {
            'cookies': 'imooc_uuid=d65724cd-5aee-483a-8b9e-49c5068a112e; imooc_isnew_ct=1513499389; imooc_isnew=2; PHPSESSID=b9lkvvjvqvsvp6erba97e1r1i4; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1515067582,1515067701,1515219683,1515392389; UM_distinctid=160ea73595919-03971df34c366d-2b0c3866-3d10d-160ea73595a1fe; page=https://coding.m.imooc.com/index.html?c=fe; connect.sid=s%3ABPMOsKGZIUOFX_q6dl6NHbvQvoi1jab_.H1bVmvNPgzYWY%2FBZFhUGUg%2F%2BZCxixZAb0fOz1UDl4xQ; CNZZDATA1261728817=1023580016-1515841800-%7C1515841800; Hm_lvt_c92536284537e1806a07ef3e6873f2b3=1515846204; Hm_lpvt_c92536284537e1806a07ef3e6873f2b3=1515846204; last_login_username=1823327404%40qq.com; IMCDNS=0; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1516157480; cvde=5a530d809504b-34'}
        new_dict = {}
        for line in cookies['cookies'].split(';'):
            key, value = line.split('=', 1)  # 分一次得到2个数据
            new_dict[key] = value

        json_data={
            'input1':username,
            'input2':psw,
            'remember':reme
        }
        res=requests.post(url,headers=headers,cookies=new_dict,json=json_data)
        print(res.content)
        print(res.json)
    def test_login1(self):
        username='13166427863',
        psw='ayQydgPDn2zPNaEC/gIyc7U9NNqzOI4TfSZq8KOX3LuBElc8anUzICIDDOnfC1leG8UkUItj8YXNVkdO5d8xBO0QdCVKo30/vZBzN1xjZDfQ8g2ufyhFrJPszWFC8I2v6VoIUYvxVHVaZRMW/5EJymEKunAdJPAmqZ5FVSOHFgc=',
        result=self.login(username,psw)
        self.assertEqual(result['success'],True)
    def test_login2(self):
        username = '13166427863',
        psw='xxx'
        result = self.login(username, psw)
        self.assertEqual(result['success'], True)

if __name__ == '__main__':
    unittest.main()