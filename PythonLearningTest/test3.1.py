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

