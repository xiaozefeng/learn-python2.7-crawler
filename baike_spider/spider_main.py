# coding:utf-8
import url_manager, html_downloader, html_outputer, html_parser
'''
爬虫入口
'''


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    ''' 
        爬虫方法
    '''

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        # 当url管理器中还有未爬取的url时，循环爬取
        while self.urls.has_new_url():
            try:
                # 从url管理器中获取一个url
                new_url = self.urls.get_new_url()
                print '%d, %s' % (count, new_url)
                # 调用下载器下载html
                html_cont = self.downloader.download(new_url)
                # 调用解析器获取解析后的数据，已经需要爬取的urls
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)
                if count == 50:
                    break
                count += 1
            except:
                print '%s craw faild' % new_url
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
