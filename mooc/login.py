import requests
class mooc():
    def __init__(self,s):
        self.s=s
    def login(self, username, psw, reme=True):
        url='https://passport.cnblogs.com/user/signin'
        headers={
            'Cookie': '_ga=GA1.2.382458561.1513424506; _gid=GA1.2.994547639.1515147240; ASP.NET_SessionId=nm0l2ig5yfbsqlcpynqdqbkd; SERVERID=fc59f0882c6e4b75dcaad92e7e90772e|1515147535|1515147275',
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
            ,'Connection':' keep - alive',
            'Content - Length': '557',
            'X - Requested - With': 'XMLHttpRequest'

        }
        json_data={
            'input1':username,
            'input2':psw,
            'remember':reme
        }
        res=requests.post(url,headers=headers,json=json_data)
        print(res.content)
        #print(res.json)
        return res.json()

