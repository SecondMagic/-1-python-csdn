#coding:utf-8
import urllib.request 
import re
import sys

def getHtmlInfo(url):
	print('url:'+url)
	return str(urllib.request.urlopen(url).read(),'utf-8')
def saveInfo(info,fileName):
	try:
		fileAll='d:\\1\\python\\'+fileName+'.txt'
		print(fileAll)
		with open(fileAll,'w',encoding='utf-8') as file_write:
			file_write.write(info)
	except:
		print('error:something faile')
def getArticleUrl(html):
		reg=r'<span class="link_title"><a href="(.+?)">'
		articleRe=re.compile(reg)
		articleUrlList=re.findall(articleRe,html)
		return articleUrlList
def getTitle(html,str):
		reg=r'<span class="link_title"><a href="'+str+'">(.+?)</a>'
		titleRe=re.compile(reg,re.S)
		titleList=re.findall(titleRe,html)
		return titleList
def getTime(html):
		reg=r'<span class="link_postdate">(.+?)</span>'
		timeRe=re.compile(reg)
		timeList=re.findall(timeRe,html)
		return timeList	
def getArticleInfo(html):
		reg=r'<div id="article_content" class="article_content tracking-ad" data-mod=popu_307  data-dsm = "post" >(.+?)</div>'
		articleRe=re.compile(reg,re.S)
		articleList=re.findall(articleRe,html)
		return articleList
htmlStr='http://blog.csdn.net'
html=getHtmlInfo("http://blog.csdn.net/yeyinglingfeng?viewmode=contents")

articleUrlList=getArticleUrl(html)
for articleUrl in articleUrlList:
	articleHtml=getHtmlInfo(htmlStr+articleUrl)
	time=getTime(articleHtml)[0].replace(':','.')
	title=getTitle(articleHtml,articleUrl)[0].replace(' ','').replace('\r\n','').replace(':',' ').replace('/',' ')
	fileName=time+' '+title
	print(fileName)
	articleInfo=getArticleInfo(articleHtml)[0]
	saveInfo(articleInfo,fileName)