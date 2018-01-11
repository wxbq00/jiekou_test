# import json
# import requests
# data={
#     'a':True,
#     'b':False,
# }
# data=json.dumps(data)
# print(data)
import requests
url="http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

}
s=requests.session()
r=s.get(url,headers=headers)
result=r.json()
data=result['data']#获取data里面的内容
print(data)
get_result=data[0]['context']
print(get_result)
if u'已签收' in get_result:
    print('success')
else:
    print('fail')
print(result)

