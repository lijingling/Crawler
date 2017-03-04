# coding=utf-8
import requests

wrongNotify = '您输入的密码错误, 请重新输入'
website = 'http://www.heibanke.com/lesson/crawler_ex01/'
index = 1
while True:
    data = {'username': 'ljl', 'password': index}
    html = requests.post(website, data).content
    if wrongNotify not in html:
        print "\n密码是: %d" % index
        break
    print "第%d次访问,密码%d错误" % (index, index)
    index += 1