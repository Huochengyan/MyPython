import urllib.request
import codecs
from lxml import etree


def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

print  ("hello world!!")
url="https://m.pipigui.cc/top.html";
response=urllib.request.urlopen(url);
html=response.read();
html=html.decode("utf-8")
save_to_file("test.html",html);
print("ok")
# print(html)
# point_start=html.find('<ul class="list_tab_img" id="resize_list">',1)
# point_end=html.find('</ul>',1);
# content=html[point_start:point_end+5]
# print(content)
# tree=etree.HTML(html)
# nodes=tree.xpath("/ul[@id='resize_list']");
# print(nodes)
# f=codecs.open("test.html","r","utf-8")
# content=f.read()
# f.close()
tree=etree.HTML(html)
print("OK")
nodes=tree.xpath(u"//ul[@id='resize_list']/li");
if len(nodes)==0:
    print("00000")
else:
    for li in nodes:
        print(li)