"""
from lxml import etree
text = '''
<div>
<ul>
<li class="item-O"><a href=”linkl. html”>first item</a><lli>
<li class=” item-1”><a href=”link2.html”>second item</a><lli>
<li class=” i tem-inactive” ><a href="link3.html ”>third item< / a></h>
<li class=” item-1 ”><a href="link4.html '’>fourth item</a><lli>
<li class ＝” item －口”＞＜ a hre于＝” links . html ”＞ fi干th item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result= etree.tostring(html)
print(result.decode('utf-8'))
"""
"""
from lxml import etree
html = etree.parse('./test.html', etree .HTMLParser())
result= etree.tostring(html)
print(result.decode('utf-8'))
"""
"""
from lxml import etree
html = etree. parse('./test.html', etree. HTMLParser())
result = html.xpath ('//*')
print(result)
# [<Element html at 0x269382f6808>, <Element body at 0x269382f68c8>, <Element div at 0x269382f6908>, <Element ul at 0x269382f6948>, <Element li at 0x269382f6988>, <Element a at 0x269382f6a08>, <Element lli at 0x269382f6a48>, <Element li at 0x269382f6a88>, <Element a at 0x269382f6ac8>, <Element lli at 0x269382f69c8>, <Element li at 0x269382f6b08>, <Element a at 0x269382f6b48>, <Element li at 0x269382f6b88>]
"""
"""
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')
print(result)
print(result[0])
#[<Element li at 0x18fe2b558c8>, <Element li at 0x18fe2b55908>, <Element li at 0x18fe2b55948>, <Element li at 0x18fe2b55988>]
# <Element li at 0x18fe2b558c8>
"""
"""
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)
#[<Element a at 0x18d70977688>, <Element a at 0x18d709776c8>, <Element a at 0x18d70977708>] 
"""
"""
from lxml import etree
html = etree. parse('./test.html', etree.HTMLParser())
result = html.xpath('//ul//a')
print(result)
#[<Element a at 0x1d1c1c447c8>, <Element a at 0x1d1c1c44808>, <Element a at 0x1d1c1c44848>]
"""
"""
from lxml import etree
html = etree. parse('./test.html', etree.HTMLParser())
result = html.xpath('//ul/a')
print(result)
#[]
"""













































































