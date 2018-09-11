# coding:UTF-8
import requests
from bs4 import BeautifulSoup
import io
'''
链接类
功能：获取页面 源代码
'''
class Connect:
    def __init__(self, link):
        self.link = link

    def connect_one(link):
        # 以下是伪造请求头，伪装成浏览器访问
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
        # r 是 request 的 Response 返回对象
        r = requests.get(link, headers=headers)
        # r.text 是获取网页源代码
        # print(r.text)
        return r

'''
提取类
功能：提取源码中所需要的数据
'''
class Extract:
    def __init__(self, request):
        self.request = request

    def extract_one(self, request):

        # 使用 BeautifulSoup 解析页面源代码
        soup = BeautifulSoup(request.text, "lxml")
        title = soup.find("h1", class_="post-title").a.text.strip()

        print(title)
        return title


class Store:
    def __init__(self, content):    # content 是从网页源码中提取的内容
        self.content = content

    def store_one(self, content):
        # 使用 io 将网页中提取的内容使用 utf-8 编码，可以解决有中文字符时的报错问题
        with io.open('title.txt', "a+",encoding="utf-8") as f:
            f.write(content)
            f.close()
