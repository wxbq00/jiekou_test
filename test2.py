
# import requests
# url="http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
#
# }
# s=requests.session()
# r=s.get(url,headers=headers)
# result=r.json()
# data=result['data']#获取data里面的内容
# print(data)
# get_result=data[0]['context']
# print(get_result)
# if u'已签收' in get_result:
#     print('success')
# else:
#     print('fail')
# print(result)
import requests
import json
# payload={
#     'key1':'value1',
#     'key2':'value2'
# }
# r=requests.get('http://httpbin.org/get',data=json.dumps(payload))
# print(r.json())

# url = 'http://httpbin.org/post'
# files = {'file': ('common/a.xlsx', open('common/a.xlsx', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# r = requests.post(url, files=files)
# print(r.text)
#
cookies = {
    'cookies': 'imooc_uuid=d65724cd-5aee-483a-8b9e-49c5068a112e; imooc_isnew_ct=1513499389; imooc_isnew=2; PHPSESSID=b9lkvvjvqvsvp6erba97e1r1i4; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1515067582,1515067701,1515219683,1515392389; UM_distinctid=160ea73595919-03971df34c366d-2b0c3866-3d10d-160ea73595a1fe; page=https://coding.m.imooc.com/index.html?c=fe; connect.sid=s%3ABPMOsKGZIUOFX_q6dl6NHbvQvoi1jab_.H1bVmvNPgzYWY%2FBZFhUGUg%2F%2BZCxixZAb0fOz1UDl4xQ; CNZZDATA1261728817=1023580016-1515841800-%7C1515841800; Hm_lvt_c92536284537e1806a07ef3e6873f2b3=1515846204; Hm_lpvt_c92536284537e1806a07ef3e6873f2b3=1515846204; last_login_username=1823327404%40qq.com; IMCDNS=0; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1516157480; cvde=5a530d809504b-34'}
new_dict={}
for line in cookies['cookies'].split(';'):
    key, value = line.split('=', 1)  # 分一次得到2个数据
    new_dict[key] = value
print(new_dict)


