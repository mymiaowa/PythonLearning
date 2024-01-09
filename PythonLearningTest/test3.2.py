"""
#get()
#调用get （）方法实现与urlopen（）相同的操作，得到一个Response对象，然后分别输出了Response的类型、状态码、响应体的类型、内容以及Cookies。
import requests
r = requests. get('https://www.baidu.com/')
print(type(r))#<class 'requests.models.Response'>
print(r.status_code)#200
print(type(r.text))#<class 'str'>
print(r.text)#html代码
print(r.cookies)#<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
"""
"""
import requests
r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/put')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
"""


"""
#get()
#一般情况下，这种信息数据会用字典来存储。那么，怎样来构造这个链接呢?这同样很简单，利用pa rams 这个参数就好了
import requests
data = {
    'name': 'germey',
    'age': 22,
}
r = requests.get('http://httpbin.org/get', params=data)
print(r. text)
"""

"""
#网页的返回类型实际上是str 类型，但是它很特殊，是JSON 格式的。
# 所以，如果想直接解析返回结果，得到一个字典格式的话，可以直接调用json （）方法。
import requests
r = requests.get('http://httpbin.org/get')
print(type(r.text))#<class 'str'>
print(r.json())
#{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.2', 'X-Amzn-Trace-Id': 'Root=1-659ced6c-5a7676df4b08b3ef6edf9bcd'}, 'origin': '114.230.227.164', 'url': 'http://httpbin.org/get'}
print(type(r.json()))#<class 'dict'>
"""

"""
import requests
import re
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
r =requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)#[]不知道为什么没有提取出来、应该要提取出所有的问题内容
"""


"""
import requests
r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
with open('favicon.ico','wb') as f:
    f.write(r.content)#同样地，音频和视频文件也可以用这种方法获取
"""

"""
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore',headers=headers)
print(r.text)
"""

"""
import requests
data ={'name':'germey','age':'22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
"""















































































































































