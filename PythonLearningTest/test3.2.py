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

"""
#请求的链接自动被构造成了:http://httpbin.org/get?name=germey&age=22
import requests
data = {
    'name': 'germey',
    'age': 22
}
r = requests.get('http://httpbin.org/get',params=data)
print(r.text)
"""
"""
#网页的返回类型实际上是str 类型，但是它很特殊，是JSON 格式的。
# 所以，如果想直接解析返回结果，得到一个字典格式的话，可以直接调用json（）方法。
import requests
r = requests.get("http://httpbin.org/get")
print(type(r.text))#<class 'str'>
print(r.json())#{'args': {}, 'headers':...
print ( type(r.json()))#<class 'dict'>
"""
"""
import requests
import re
#User- Agent,也就是浏览器标识信息。如果不加这个，知乎会禁止抓取。
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
r =requests.get ("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern, r.text)
print(titles)
# []
"""
"""
import requests
r = requests.get("https://github.com/favicon.ico")
print(r. text)
print(r.content)
"""
"""
#用了open （）方法，它的第一个参数是文件名称，第二个参数代表以二进制写的形式打开，可以向文件里写入二进制数据。
import requests
r = requests.get("https://github.com/favicon.ico")
with open ('favicon.ico','wb') as f:
    f.write(r.content)
"""
"""
import requests
r = requests.get("https://www.zhihu.com/explore")
print(r.text)#书上说不能正常请求，但实操中可以正常请求
"""
"""
import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore",headers=headers)
print(r.text)#依旧可以正常请求，也不知道为什么
"""
"""
#POST前面我们了解了最基本的GET请求另外一种比较常见的请求方式是POST 。使用request实现POST请求同样非常简单
import requests
data ={'name':'germey','age':'22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
"""
"""
import requests
r = requests.get('http://www.jianshu.com')
print(type(r.status_code), r.status_code)#<class 'int'> 403
print(type(r.headers), r.headers)#<class 'requests.structures.CaseInsensitiveDict'> {'Date': 'Wed, 10 Jan 2024 02:18:58 GMT',
print(type(r.cookies), r.cookies)#<class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[]>
print(type(r.url), r.url)#<class 'str'> https://www.jianshu.com/
print(type(r.history), r.history)#<class 'list'> [<Response [302]>]
"""
"""
import requests
r = requests.get("http://www.jianshu.com")
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
"""
"""
import requests
files = {'file': open('favicon.ico','rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)
"""
"""
#cookies
#首先调用ιoo ki es 属性即可成功得到Cookies ， 可以发现它是Reque s tCooki e J ar 类型。
# 然后用item s （）方法将其转化为元组组成的列表， 遍历输出每一个Cookie 的名称和值， 实现Cookie
# 的遍历解析。
import requests
r = requests.get("https://www.baidu.com")
print(r.cookies)
for key,value in r.cookies.items():
    print(key + '=' + value)
#<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
# BDORZ=27315
"""
"""
import requests
headers = {
    'Cookie':'82AE7E8B625D6C96AA26712FBC71D8A2',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)
"""
"""
#分割cookies
import requests
cookies = 'ID=a12293c6cf3e9e7b-22b24f6221dd00ea:T=1681119230:RT=1696333171:S=ALNI_MYurEoPXZCgFw3imSqistthIZ5bdQ'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
for cookie in cookies.split(':'):
    key,value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
print(r.text)
"""
"""
#维持同一个会话， 也就是相当于打开一个新的浏览器选项
# 卡而不是新开一个浏览器。但是我又不想每次设置cook ies ，那该怎么办呢？这时候就有了新的
# 利器一－ Session 对象。
# 利用它，我们可以方便地维护一个会话，而且不用担心cookies 的问题，它会帮我们自动处理好。
import requests
requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)
#这里我们请求了一个测试网址htψ ： ／岛tψbin.org/ cookies/set/number/ 1234 567 89 。请求这个网址时，
# 可以设置一个cookie ，名称叫作number ，内容是123456789 ，随后又请求了htφ ： ／/httpbin.org/cookies,
# 此网址可以获取当前的C ookies 。
# {
#   "cookies": {}
# }
#这样并不能成功获取到设置的Cookies
"""
"""
#Session
import requests
s = requests.Session()
s .get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
#{
  # "cookies": {
  #   "number": "123456789"
  # }
# }
#这样能成功获取到设置的Cookies
"""
"""
import requests
response = requests.get('https://www.12306.cn')
print(response.status_code)#200
"""
"""
import requests
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)# Adding certificate verification is strongly advised.
"""
"""
import requests
from requests.packages import urllib3
urllib3.disable_warnings()#设置忽略警告
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)#200
"""
"""
import logging
import requests
logging.captureWarnings(True)#或者通过捕获警告到日志的方式忽略警告
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)#200
"""
"""
import requests
response = requests.get('https://www.12306.cn', cert=('/path/server.crt','/path/key'))#报错
print(response.status_code)
"""
"""
import requests
proxies = {
    "http":"http://110.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}
requests.get("https://www.taobao.com",proxies=proxies)
#直接运行这个实例可能不行，因为这个代理可能是无效的，请换成自己的有效代理试验
# 一下。
"""
"""
#若代理需要使用HTTP Basic Auth ，可以使用类似http://user: password@host: port 这样的语法来设
# 置代理，示例如下：
import requests
proxies = {
    "http":"http://user:password@10.10.1.10:3128/",
}
requests.get("https://www.taobao.com",proxies=proxies)
"""
"""
# pip3 install 'requests[socks]'
#除了基本的HTTP 代理外， requests 还支持SOCKS 协议的代理。
# SOCKS 协议代理
import requests
proxies = {
    'http':'socks5://user:password@host:port',
    'https':'socks5://user:password@host:port'
}
requests.get("https://www.taobao.com",proxies=proxies)
"""
#在本机网络状况不好或者服务器网络响应太慢甚至无响应时，我们可能会等待特别久的时间才可
# 能收到响应，甚至到最后收不到响应而报错。为了防止服务器不能及时响应，应该设置一个超时时间，
# 即超过了这个时间还没有得到响应，那就报错。这需要用到timeout 参数。这个时间的计算是发归请
# 求到服务器返回响应的时间。
"""
import requests
r = requests.get("https://www.taobao.com",timeout=1)#将超时时间设置为1秒，如果1秒内没有响应，那就抛异常。
print(r.status_code)#200
"""
# 请求分为两个阶段，即连接（ connect ）和读取（ read ）。
# 上面设置的timeout 将用作连接和读取这二者的timeout 总和。
# 如果要分别指定，就可以传入一个元组：
#r = requests.get ("https://www.taobao.com", timeout=(S,11, 30))
# 如果想永久等待，可以直接将timeout 设置为None ，或者不设置直接留空，因为默认是None 。这
# 样的话，如果服务器还在运行，但是响应特别慢，那就慢慢等吧，它永远不会返回超时错误的。其用
# 法如下：
# r = requests.get("https://www.taobao.com", timeout=None)
"""
import requests
from requests.auth import HTTPBasicAuth
r = requests.get('http://localhost:5000', auth=HTTPBasicAuth ('username','password'))
print(r.status_code)#身份认证,由于目标计算机积极拒绝，无法连接。
"""
"""
import requests
r = requests.get('http://localhost:5000', auth =('username','password'))
print(r.status_code)#由于目标计算机积极拒绝，无法连接。
"""
"""
import requests
from requests_Oauthlib import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY',' YOUR_APP_SECRET',
'USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)#ModuleNotFoundError: No module named 'requests_Oauthlib'
"""
"""
#Prepared Request
#前面介绍urllib 时，我们可以将请求表示为数据结构，其中各个参数都可以通过一个Request 对
# 象来表示。这在requests 里同样可以做到，这个数据结构就叫Prepared Request 。
from requests import Request, Session
url ='http://httpbin.org/post'
data = {
'name':'germey'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
s = Session()
req = Request ('POST', url, data =data, headers= headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
"""


































































































































































































































































