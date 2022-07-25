
import requests

import lxml.html


class Openurl:
    # 从文件中读取博主地址链接
    url=[]
    def __init__(self,fielname):
        file=open(fielname,'r',encoding="UTF-8")
        i=True
        while(i):
            context=file.readline()
            if(context in 'end\n'):
                i=False
            else :
                self.url.append(context)

class indexurl:

    url=[]
    # 存储每个文章的url
    title=[]
    # 存储每个文章的标题
    size=[]
    # 存储每个文章的访问量
    def __init__(self,index):
        self.op(index)
        
    def op(self,index):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

        response=requests.get(index,headers=headers)
        response.elapsed='utf-8'
        html=response.text

        name='//*[@id="userSkin"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/text()'
        # 定位资源 文章链接
        xpathurl='//a[@target="_blank"]/@href'

        html = lxml.html.fromstring(html)
        self.url = html.xpath(xpathurl)
        print("当前博主：",html.xpath(name))

class gogogo:
    url=''
    def __init__(self,url):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

        response=requests.get(url,headers=headers)


