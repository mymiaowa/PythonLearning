# import urllib.request
# response= urllib.request.urlopen('https://www.taobao.com/')
# print(response. read(). decode ('utf-8'))

#请求方式POST
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word':'ipad air5'}), encoding = 'utf8')
# response = urllib.request.urlopen('https://www.taobao.com/', data=data)#data参数是传给服务器的，post推给服务器
# print(response.read())
from urllib.error import URLError
import http.cookiejar, urllib.request
#需要模拟登录
#https://zhuanlan.zhihu.com/p/558559680
if __name__ == '__main__':
    #构建一个CookieJar对象实例来保存cookie
    cookie = http.cookiejar.CookieJar()
    #使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
    handler = urllib.request.HTTPCookieProcessor(cookie)
    #通过build_opener()来构建opener
    opener = urllib.request.build_opener(handler)
    #以get方法访问页面，访问之后会自动保存cookie到cookiejar中
    response = opener.open('https://www.taobao.com')
    try:
        #可以按照标准格式将保存的Cookie打印出来
        for item in cookie:
            print(item.name+"="+item.value)
    except URLError as e:
        print(e.reason)




























































































