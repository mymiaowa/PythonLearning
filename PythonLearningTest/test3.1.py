"""
import urllib.request
response= urllib.request.urlopen('https://www.python.org')
#GET 请求抓取
#urllib.request.urlopen(url, data=None, [ timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# print(response. read(). decode ('utf-8'))
# print(type(response)) #<class 'http.client.HTTPResponse'>
print(response.status) #200
print(response.getheaders()) #一大堆元组[('Server', 'nginx'),...]
print(response.getheader('Server')) #nginx
"""

"""
#请求方式POST
import urllib.parse
import urllib.request
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding = 'utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
"""

"""
#该异常属于urllib. error 模块，错误原因是超时。
#设置超时时间是l 秒。程序l 秒过后，服务器依然没有响应，于是抛出了U RL Error 异常。
import urllib.request
response = urllib.request . urlopen ('http://httpbin.org/get', timeout=1)
print(response.read())
"""


"""
import socket
import urllib.request
import urllib.error
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT') #TIME OUT
"""
"""
import urllib.request
request = urllib.request.Request ('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
"""
"""
from urllib import request, parse
url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host':'httpbin.org'
}
dict = {
    'name':'Geimey',
}
data= bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method ='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
"""

"""
from urllib import request, parse
url = 'http://httpbin.org/post'
dict = {
    'name':'Geimey',
}
data= bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
"""

"""
#弹出提示框，直接提示你输入用户名和密码，验证成功后才能查看页面
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
username = 'username'
password = 'password'
url = 'http://localhost:5000/'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
try:
    result = opener.open(url)
    html = result.read().decode ('utf8')
    print(html)
except URLError as e:
    print(e.reason)#[WinError 10061] 由于目标计算机积极拒绝，无法连接。
"""

"""
#添加代理:在本地搭建了一个代理，它运行在9743 端口上
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
})#使用了ProxyHandler,其参数是一个字典,键名是协议类型（比如HTTP 或者HTTPS 等）,键值是代理链接，可以添加多个代理。
#利用这个Handler 及build_opener()方法构造一个Opener ，之后发送请求即可
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode ('utf-8'))
except URLError as e:
    print(e.reason)#[WinError 10061] 由于目标计算机积极拒绝，无法连接。
"""

"""
import http.cookiejar, urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)
#这里输州了每条Cookie的名称和值
# BAIDUID=3121DCD21AF139A4BD84D9E551F8D761:FG=1
# BIDUPSID=3121DCD21AF139A4F4A002DE573540BF
# PSTM=1704701434
"""

"""
import http.cookiejar, urllib.request
filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
"""

"""
import http.cookiejar, urllib.request
filename = 'cookies2.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)要保存成LWP 格式的Cookies 文件，可以在声明时就改为：
cookie = http. cookiejar. LWPCookieJar (filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
"""

"""
#，生成了Cookies文件(cookies2.txt)后，怎样从文件(cookies2.txt)中读取并利用呢？
import http.cookiejar, urllib.request
cookie = http.cookiejar.LWPCookieJar()
#这里调用load()方法来读取本地的Cookies文件，获取到了Cookies的内容
#前提是我们首先生成了LWPCookieJar 格式的Cookies ，并保存成文件，
#然后读取Cookies 之后使用同样的方法构建Handler 和l Opener 即可完成操作
cookie.load('cookies2.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib .request.build_opener(handler)
response= opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))#运行结果正常的话，会输出百度网页的源代码
"""

