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

"""
from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)#Not Found
"""

"""
from urllib import request,error
try:
    response = request. urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers)#, sep='\n'
#依然是同样的网址，这里捕获了HTTP Error 异常，输出了reason 、code 和headers 属性。
"""

"""
from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
#这样就可以做到先捕获HTTP Error ，获取它的错误状态码、原因、headers 等信息。如果不是
#HTTP Error 异常，就会捕获URLError 异常，输出错误原因。最后，用else 来处理正常的逻辑。这是一个较好的异常处理写法。
"""

"""
import socket
import urllib.request
import urllib.error
try:
    response = urllib.request.urlopen ('https://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
        #<class 'socket.timeout'>
        #TIME OUT
"""

"""
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
#<class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
"""

"""
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep ='\n')
# http
# http
# www.baidu.com
# www.baidu.com
"""

"""
# urlunparse
from urllib.parse import urlunparse
data =['http','www.baidu.com', 'index.html','user','a=6','comment']
print(urlunparse(data))#http://www.baidu.com/index.html;user?a=6#comment  成功实现了URL 的构造,长度必须是6
"""

"""
# urlsplit
from urllib.parse import urlsplit
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
#SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
#返回结果是SplitResult ， 它其实也是一个元组类型， 既可以用属性获取值，也可以用索引来获取。
"""

"""
# urlsplit
from urllib.parse import urlsplit
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result.scheme,result[0])#http http
"""

"""
#urlunsplit()与urlunparse()类似，唯一的区别是长度必须为5
from urllib.parse import urlunsplit
data =['http','www.baidu.com', 'index.html','a=6','comment']
print(urlunsplit(data))
#http://www.baidu.com/index.html?a=6#comment
#有了urlunparse （）和urlunsplit （）方法，我们可以完成链接的合井，不过前提必须要有特定长度的对象，
#链接的每一部分都要清晰分开。
"""

"""
#urljoin()
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com', 'FAQ.html'))#http://www.baidu.com/FAQ.html
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))#https://cuiqingcai.com/FAQ.html
print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))#https://cuiqingcai.com/FAQ.html
print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html?question=2'))#https://cuiqingcai.com/FAQ.html?question=2
print(urljoin('http://www.baidu.com,wd=abc','https://cuiqingcai.com/index.php'))#https://cuiqingcai.com/index.php
print(urljoin('http://www.baidu.com','?category=2#comment'))#http://www.baidu.com?category=2#comment
print(urljoin('www.baidu.com','?category=2#comment'))#www.baidu.com?category=2#comment
print(urljoin('www.baidu.com#comment','?category=2'))#www.baidu.com?category=2
#可以发现， base_url 提供了三项内容scheme 、netloc 和path 。如果这3 项在新的链接里不存在，
#就予以补充；如果新的链接存在，就使用新的链接的部分。而base_url 中的pa rams 、query 和fragment是不起作用的。
"""

"""
#urlencode()
from urllib .parse import urlencode
params = {
    'name': 'germey',
    'age' : 22,
}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)#http://www.baidu.com?name=germey&age=22
"""

"""
#parse_qs()
from urllib.parse import parse_qs
query= 'name=germey&age=22'
print(parse_qs(query))
#{'name': ['germey'], 'age': ['22']}
#有一串GET请求参数,利用parse_qs()方法,就可以将它转回字典
"""

"""
#parse_qsl()
#它用于将参数转化为元组组成的列表
from urllib.parse import parse_qsl
query= 'name=germey&age=22'
print(parse_qsl(query))
#[('name', 'germey'), ('age', '22')]
"""

"""
#quote()
#URL 中带有中文参数时，有时可能会导致乱码的问题，此时用这个方法可以将巾文字符转化为URL编码
from urllib.parse import quote
keyword = '壁纸'
url ='https://www.baidu.com/s?wd ='+ quote(keyword)
print(url)#https://www.baidu.com/s?wd =%E5%A3%81%E7%BA%B8
"""

"""
#unquote()
#有了quote()方法，当然还有unquote()方法，它可以进行URL解码
from urllib.parse import unquote
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))#https://www.baidu.com/s?wd=壁纸
"""
#Robots 协议
#User-agent 描述了搜索’爬虫的名称，这里将其设置为＊则代表该协议对任何爬取爬虫有效。
#Disallow 指定了不允许抓取的目录，比如上例子中设置为／则代表不允许抓取所有页面。
#Allow 一般和Disallow 一起使用，一般不会单独使用，用来排除某些限制。现在我们设置为/public／，
# 则表示所有页面不允许抓取，但可以抓取public 目录。

"""
from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=l&type=collections'))
# False
# False利用can_fetch （）方法判断了网页是否可以被抓取。
"""


# set_url():用来设置ro bots . txt 文件的链接。如果在创建RobotFileParser 对象时传入了链接，那么就不需要再使用这个方法设置了。
#read （）： 读取robots .txt 文件并进行分析。注意，这个方法执行一个读取和分析操作，如果不调用这个方法，
# 接下来的判断都会为False ，所以一定记得调用这个方法。这个方法不会返回任何内容，但是执行了读取操作。
#parse （）： 用来解析robots.txt文件，传人的参数是robots.txt 某些行的内容，它会按照robots.txt的语法规则来分析这些内容。
#can_fetch （）： 该方法传人两个参数， 第一个是Use r-age nt ，第二个是要抓取的URL 。
# 返回的内容是该搜索引擎是否可以抓取这个URL ，返回结果是True 或False
#mtime （）： 返回的是上次抓取和分析robots.txt 的时间，这对于长时间分析和抓取的搜索爬虫是很有必要的，
# 你可能需要定期检查来抓取最新的robots.txt 。
#modified （） ：它同样对长时间分析和抓取的搜索爬虫很有帮助，将当前时间设置为上次抓取和分析robots.txt 的时间。

"""
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
rp = RobotFileParser()
rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=l&type=collections'))
#urllib.error.HTTPError: HTTP Error 403: Forbidden
"""






