'''Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36
username:XXX
password:XXX
rememberMe:true
lt:LT-228603-HxwpYPt7DFMlsLbnGJ7WdKg4M7a0e1
execution:e3s1
_eventId:submit'''
# -*- coding: utf-8 -*-
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path

	
# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'
headers = {
    "Host": "passport.csdn.net",
    "Referer": "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn",
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
    print("Cookie 加载")
except:
    print("Cookie 未能加载")
	
index_url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
# 获取登录时需要用到的lt
index_page = session.get(index_url, headers=headers)
html = index_page.text
	
def getlt():
    pattern = r'name="lt" value="(.*?)"'
    # 这里的lt 返回的是一个list
    lt = re.findall(pattern, html)
    print(lt[0])
    return lt[0]
	
def getExecution():
    pattern = r'name="execution" value="(.*?)"'
    # 这里的execution 返回的是一个list
    execution = re.findall(pattern, html)
    print(execution[0])
    return execution[0]

def get_eventId():
    pattern = r'name="_eventId" value="(.*?)"'
    # 这里的_eventId 返回的是一个list
    _eventId = re.findall(pattern, html)
    print(_eventId[0])
    return _eventId[0]

def login(secret, account):
    #headers["lt"]=getlt()
    #headers["execution"]=getExecution()
    #headers["_eventId"]=get_eventId()	
    post_url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
    postdata = {
        'lt': getlt(),
        'execution': getExecution(),
        '_eventId': get_eventId(),
		'password': account,
		'username': secret
		#'rememberMe': 'true'
    }
    print(postdata)
	# 不需要验证码直接登录成功
    login_page = session.post(post_url, data=postdata, headers=headers)
    print(login_page.text)
    #login_code = login_page

    #print(session.get('http://msg.csdn.net/').text)
	 # 保存 cookies 到文件，
    # 下次可以使用 cookie 直接登录，不需要输入账号和密码
    session.cookies.save()
def isLogin():
    # 通过查看个人信息来判断是否已经登录
    url = "http://msg.csdn.net/"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    print(login_code)
    if login_code == 200:
        return True
    else:
        return False
if __name__ == '__main__':
    if isLogin():
        print('已登入')
    else:
        login('XXX','XXX')