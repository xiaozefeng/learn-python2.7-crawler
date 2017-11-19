#coding: utf-8
# import urllib2
import requests

'''
文档下载
'''
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        res = requests.get(url)
        if res.status_code != 200:
            return None
        return res.text

    # def download(self, url):
    #     if url is None:
    #         return None
    #     res = urllib2.urlopen(url)
    #     if res.getcode() != 200:
    #         return None
    #     return res.read()
