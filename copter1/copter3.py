# coding=utf-8
import requests

website1 = 'http://www.heibanke.com/accounts/login'
website2 = 'http://www.heibanke.com/lesson/crawler_ex02'
wrongNotify = '您输入的密码错误, 请重新输入'

s = requests.Session()
s.get(website1)     # 访问登录页面获取登录要用的csrftoken
token1 = s.cookies['csrftoken']      # 保存csrftoken

dataWebsite1 = {'username': 'ljlljlljl',
                'password': '111111',
                'csrfmiddlewaretoken': token1
                }
s.post(website1, data=dataWebsite1)

pwd = 1
while pwd < 30:
    # 以下步骤原理和上面一样
    s.post(website2)
    token2 = s.cookies['csrftoken']
    dataWebsite2 = {'username': 'ljl',
                'password': pwd,
                'csrfmiddlewaretoken': token2
                }
    result = s.post(website2, data=dataWebsite2)
    if wrongNotify in result.content:
        print '密码%d错误' % pwd
        pwd += 1
    else:
        print '密码是%d' % pwd
        break