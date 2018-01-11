import unittest
import requests
class test_kuaidi(unittest.TestCase):
    def setUp(self):
        self.headers={
            'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 63.0.3239.108Safari / 537.36'
        }
    def chaxun_yunda(self,danhao,kd,company):
        # danhao='1202247993797'
        # kd='yunda'
        self.url='http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html'%(danhao,kd)
        print(self.url)
        r=requests.post(self.url,headers=self.headers)#发请求
        result=r.json()
        print(result['company'])
        data=result['data']
        get_result=data[0]['context']
        self.assertIn(u'已签收',get_result)
        self.assertEqual(company,result['company'])
    def test_kuaidi(self):
        danhao = '1202247993797'
        kd='yunda'
        company=u'韵达快递'
        self.chaxun_yunda(danhao,kd,company)
if __name__ == '__main__':
    unittest.main()
