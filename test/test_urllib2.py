# coding:utf-8
import urllib2, cookielib

url = 'http://www.baidu.com'
print '第一种方法'
res1 = urllib2.urlopen(url)
print res1.getcode()
print len(res1.read())

print '第二种方法'
request = urllib2.Request(url)
request.add_header('user-agent','Mozilla/5.0')
res2 = urllib2.urlopen(request)
print res2.getcode()
print len(res2.read())

print '第三种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
res3 = urllib2.urlopen(url)
print res3.getcode()
print cj
# print res3.read()
