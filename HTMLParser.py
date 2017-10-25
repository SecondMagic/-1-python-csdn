#coding:utf-8
from html.parser import HTMLParser
import urllib.request 
import re
import sys

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.articleStr = []
        self.check='N'
        self.num=0
    def handle_starttag(self, tag, attrs):
        if tag =='a':
            if len(attrs)==1 and attrs[0][0]=='href' and '/yeyinglingfeng/article/details/' in attrs[0][1] and '#comments' not in attrs[0][1]:
                self.check='Y'
                article={}
                article['url']='http://blog.csdn.net'+attrs[0][1]
                self.articleStr.append(article)
                self.num+=1
    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        if self.check=='Y':
            self.articleStr[-1]['articleTitle']=data.replace('\r\n','').strip()
            self.check='N'
    def handle_startendtag(self, tag, attrs):
        pass
    def handle_comment(self,data):
        pass		
def getHtmlInfo(url):
	print('url:'+url)
	return str(urllib.request.urlopen(url).read(),'utf-8')
def saveInfo(info):
	try:
		with open('d:\\1\\csdnList.txt','w',encoding='utf-8') as file_write:
			file_write.write(info)
	except:
		print('error:something faile')	
html=getHtmlInfo("http://blog.csdn.net/yeyinglingfeng?viewmode=contents")
parser = MyHTMLParser()
parser.feed(html)
parser.close()
allInfo=''
for each in parser.articleStr:
    allInfo+=each['articleTitle']+' url:'+each['url']+'\n'
#print(allInfo)
saveInfo(allInfo)
print(str(parser.num))