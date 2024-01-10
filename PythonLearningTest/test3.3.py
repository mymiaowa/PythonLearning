"""
#match()
import re
content ='Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match ('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())
# 41
# <re.Match object; span=(0, 25), match='Hello 123 4567 World_This'>
# Hello 123 4567 World_This
# (0, 25)
"""
"""
import re
content ='Hello 123 4567 World_This is a Regex Demo'
result = re.match ('Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
# <re.Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
# Hello 123 4567 World_This is a Regex Demo
# (0, 41)
"""
"""
import re
content ='Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))
#7
# 涉及一个贪婪匹配与非贪婪匹配的问题了。在贪婪匹配下,.＊会匹配尽可能多的字符。
# 正则表达式中．＊后面是＼d＋，也就是至少一个数字，并没有指定具体多少个数字，因此，.＊就尽可能匹配多的字符，
# 这里就把123456 匹配了,给＼d＋留下一个可满足条件的数字7 ，最后得到的内容就只有数字7 了。
"""
"""
#非贪婪匹配的写法是.*?,多了一个?
import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
# <re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
# 1234567
#贪婪匹配是尽可能匹配多的字符，非贪婪匹配就是尽可能匹配少的字符。
# 当.＊？匹配到Hello 后面的空向字符时，再往后的字符就是数字了，而＼ d+恰好可以匹配，
# 那么这里．.*?的就不再进行匹配，交给＼ d ＋去匹配后面的数字。所以这样.*?匹配了尽可能少的字符，
# ＼ d ＋的结果就是1234567 了。
"""
"""
# 在做匹配的时候，字符串中间尽量使用非贪婪匹配，也就是用.*?叫来代替.*,以免出现匹配结果缺失的情况。
#但这里需要注意，如果匹配的结果在字符串结尾，.*?就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符。
import re
content ='http://weibo.com/comment/kEraCN'
resultl = re.match('http.*?comment/(.*?)',content)
result2 = re.match('http.*?comment/(.*)',content)
print('resultl', resultl. group(1))
print('result2', result2. group(1))
# result1
# result2 kEraCN
#可以观察到,.*?没有匹配到任何结果,而.*则尽量匹配多的内容，成功得到了匹配结果。
"""
"""
import re
content ='''Hello 1234567 World_This 
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$',content)
print(result.group(1))
# AttributeError: 'NoneType' object has no attribute 'group'
# 为什么加了一个换行符，就匹配不到了呢？这是因为．匹配的是除换行符之外的任意字符，
# 当遇到换行符时,.*?就不能匹配了，所以导致匹配失败。这里只需加一个修饰符re.S ，即可修正这
# 个错误,这个修饰符的作用是使．匹配包括换行符在内的所有字符。
"""
"""
# re.S
import re
content ='''Hello 1234567 World_This 
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
print(result.group(1))#1234567
# 这个re.S 在网页匹配中经常用到。因为HTML节点经常会有换行，加上它，就可以匹配节点与节点之间的换行了。
#re.I使匹配对大小写不敏感
"""
"""
import re
content ='(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com',content)
print(result)
#<re.Match object; span=(0, 17), match='(百度)www.baidu.com'>
"""
"""
#search()
import re
content= 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo',content)
print(result)#None
#这里的字符串以Extra开头，但是正则表达式以Hello 开头，整个正则表达式是字符串的一部分，但是这样匹配是失败的。
#因为match （）方法在使用时需要考虑到开头的内容，这在做匹配时并不方便。
# 它更适合用来检测某个字符串是存符合某个正则表达式的规则。
#这里就有另外一个方法search （），它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果。
# 也就是说，正则表达式可以是字符串的一部分，在匹配时， search （）方法会依次扫描字符串，
# 直到找到第一个符合规则的字符串，然后返回匹配内容，如果搜索完了还没有找到，就返回None 。
import re
content= 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo',content)
print(result)
# <re.Match object; span=(13, 53), match='Hello 1234567 World_This is a Regex Demo'>
"""
"""
#findall()
# 介绍了search （）方法的用法，它可以返回匹配正则表达式的第一个内容，但是如果想要
# 获取匹配正则表达式的所有内容，那该怎么办呢？这时就要借助findall （）方法了。该方法会搜索整
# 个字符串，然后返回匹配正则表达式的所有内容。
import re
html = '''< div id="songs-list" >
<h2 class ＝title >经典老歌</ h2>
<p class="introduction">
经典老歌列表
</p>
<ul id=” list” class=” list-group”>
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href ＝"/2.mp3" singer ＝"任贤齐"〉沧海一声笑</a>
</li>
<li data-view=” 4 ” class=” active">
。href ＝”／ 3 .mp3 ” singer ＝”齐泰”〉往事随风＜ la>
</li>
<li data-view ＝飞”＞＜ a href="/4.mp3 ” singer＝” beyo nd ＂＞尤辉岁月＜／ a><lli>
<li data-view=” 5”>< a href="/S.mp3 ” singer~ ”除A也琳”〉记事本＜／ a><lli>
<li data-view=” 5’'>
。href ＝”／ 6.mp3 ” singer ＝”邓丽君、但愿人长久＜ l a>
</li>
</ul>
</div>'''
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?</a>)',html,re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])
"""
"""
#sub()
# 除了使用正则表达式提取信息外，有时候还需要借助它来修改文本。比如，想要把一串文本中的
# 所有数字都去掉，如果只用字符串的replace （）方法，那就太烦琐了，这时可以借助sub （）方法。示例
# 如下：
import re
content ='54aKS4yrsoiRS4ixSL2g'
content = re.sub ('\d+','', content)
print(content)#aKSyrsoiRSixSLg
#这里只需要给第一个参数传入＼ d＋来匹配所有的数字，第二个参数为替换成的字符串（如果去掉
# 该参数的话，可以赋值为空），第三个参数是原字符串。
"""
"""
#compile()
#介绍一下compile （）方法，这个方法可以将正则字符串编译成正则表达式对象
import re
contentl = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re . compile ('\d{2}:\d{2}')
result1 = re.sub(pattern,'', contentl)
result2 = re.sub(pattern,'', content2)
result3 = re.sub(pattern,'', content3)
print(result1, result2, result3)
#2016-12-15  2016-12-17  2016-12-22
"""


































