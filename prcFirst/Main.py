from prcFirst.first import *


class Main:
    def __init__(self, link):
        self.link = link

    '''
    进行第一次实验的主函数，分别调用 获取页面内容、提取数据 、存储数据 三大类的响应函数(以_one结尾)
    '''
    def main_One(self):
        request = Connect.connect_one(self.link)
        content = Extract.extract_one(self, request)
        Store.store_one(self, content)


if __name__ == '__main__':
    link = "http://" + input("请输入要爬取的网址链接：\n") + "/"
    if len(link) >= 10:
        print(link + "\n")
    if len(link) < 10:
        link = "http://www.santostang.com/"
        print("使用默认爬取地址 {0} \n {1}".format(link, '-'*50))
    main = Main(link)
    main.main_One()