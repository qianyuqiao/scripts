#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import urllib
from bs4  import BeautifulSoup as sp
import re
import os
import traceback
from bs4.element import NavigableString
import requests
import json

def get_data(pageNum):
    #爬取一页动态加载的数据,以html的形式展示,方便解析
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-language': "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    s=requests.Session()
    s.headers=headers
    post_data={'reviewType':'0','pageNum':0,'id':'com.google.android.youtube','reviewSortOrder':'4','xhr':'1','token':'yXsAwboFTBTlbycevc5OfQ178dI:1520937083085'}
    post_data['pageNum']=str(pageNum)
    r = s.post('https://play.google.com/store/getreviews?authuser=0',data=post_data,verify=False)
    
    html_text = r.text.decode('unicode-escape').encode('utf-8').replace('\n','').replace('[["ecr",1,','').replace(')]}\'"','').replace('",'+str(pageNum)+']]','')
    html_text='<html><body>'+html_text
    html_text+='</body></html>'
    
    f=open('d:/googleplaycomments'+str(pageNum)+'.html','w')
    f.write(html_text)
    f.close()
    
    print 'done'

def http_get(url,timeout=None):
    header={
    
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'accept-language': "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    req=urllib2.Request(url,headers=header)
    
    if timeout:
        result= urllib2.urlopen(req,timeout).read()
    else:
        result= urllib2.urlopen(req).read()
    return result
    
    
global count
count=0
def parse_google_play(html):
    global count
    ##爬取静态html
    soup=sp(html,'html.parser')
    body_content =soup .find('div',class_='body-content')
    main_content=body_content.find('div',class_='main-content')
    apps=main_content.find('div',class_='details-wrapper apps')
    details=apps.find('div',class_='details-section reviews')
    details_section_contents=details.find('div',class_='details-section-contents')
    details_section_body= details_section_contents.find('div',class_='expandable')
    
    multicol = details_section_body.find('div',class_='all-reviews multicol')
    featured_review = multicol.find_all('div',class_ ='single-review' )
    
    f=open('d:/static_html_content.txt','w')
    for tag in featured_review:
        author_name = tag.find('span','author-name')
        tag_text=tag.find('div','review-body with-review-wrapper')
        count+=1
        s=str('name: '+author_name.get_text().decode('utf-8')+' review: '+tag_text.get_text().decode('utf-8'))
        print s
        f.write(s+'\n')
    f.close()

    
def get_datas():
    for i in range(100):
        get_data(i)
    
    
def main():
    
    url='https://play.google.com/store/apps/details?id=com.facebook.katana'
    print 'begin downloading!'
    html=http_get(url)
    f=open('d:/codes/googleplay.html','w')
    f.write(html)
    f.close()
    print 'download finished!'
    print 'begin parsing....'
    print 'begin parsing static html'
    parse_google_play(html)
    print 'static html parsing finished, begin getting more datas'
    get_datas()
    
if __name__ == '__main__':
    print '开始'.decode('utf-8')
    get_datas()
