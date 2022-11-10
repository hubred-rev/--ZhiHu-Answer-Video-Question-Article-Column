import requests as r
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time,os
import sys
from html.parser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()
def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text
'''
br=wd.Firefox()
token='lao-liang-83-95'
br.get('https://www.zhihu.com/people/%s/answers'%token)
br.find_element(By.XPATH,'//*[@class="SignFlow-tab"]').click()
br.find_element(By.XPATH,'//*[@class="Input username-input"]').send_keys('13841330162')
br.find_elements(By.XPATH,'//*[@class="Input username-input"]')[1].send_keys('3254722,AB')
br.find_element(By.XPATH,'//*[@class="Button SignFlow-submitButton Button--primary Button--blue"]').click()
'''
'''
h=[a.split('"')[0]for a in r.get('https://www.zhihu.com/people/gong-ge-cheng-52/answers').text.split('/question/')[1:]]
print(h)
'''
'''
br=wd.Firefox()
br.get('https://www.zhihu.com/people/gong-ge-cheng-52/columns')
cl=br.find_element(By.XPATH,'//*[@class="Button Modal-closeButton Button--plain"]')
if cl:cl.click()
br.find_element(By.XPATH,'//*[@aria-controls="Profile-posts"]').click()
'''
#os.system('google-chrome --remote-debugging-port=9222 --user-data-dir="/home/a/Pictures/ZhiHu AQVA/indexs"')
bp=Options()
bp.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
br=wd.Chrome(options=bp)
dd='lao-liang-83-95'
tags=['columns','posts','asks','zvideos','answers']
disable={'columns':'<div>还没有文章</div>','posts':None,'asks':None,'zvideos':None,'answers':None}
nm={}
for a in tags:
    li='https://www.zhihu.com/people/%s/%s'%(dd,a)
    br.get(li)
    time.sleep(2)
    '''
    cl=br.find_element(By.XPATH,'//*[@class="Button Modal-closeButton Button--plain"]')
    if cl:cl.click()
    br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    '''
    h=br.page_source
    #print(h.find('下一页</button>'))
    if'<button type="button" class="Button PaginationButton PaginationButton-next Button--plain">下一页</button>'in h:
        nm[a]=int(h.split('<button type="button" class="Button PaginationButton PaginationButton-next Button--plain">下一页</button>')[0].split('</button>')[-2:][0].split('>')[1])
    else:nm[a]=1
    if disable[a]:
        if disable[a]in h:nm[a]=0
    print('%s列表總共有%d頁。'%(a,nm[a]))
for a in nm.keys():
    n=0
    for b in range(nm[a]):
        li='https://www.zhihu.com/people/%s/%s?page=%s'%(dd,a,nm[a]-b)
        n+=1
        br.get(li)
        time.sleep(3)
        ed='indexs/%s/%s.list'%(a,str(n).rjust(6).replace(' ','0'))
        if not os.path.exists(pa:='/'.join(ed.split('/')[:-1])):os.makedirs(pa)
        h=br.page_source
        if a=='columns':
            h=[eval(dehtml(c.split('"')[0]))for c in h.split('data-za-extra-module="')[1:]]
        elif a=='posts':
            h=[{'data-zop':eval(dehtml(c.split('"')[0]))}for c in h.split('data-zop="')[1:]]
        elif a=='asks':
            h=[eval(dehtml(c.split('"')[0]))for c in h.split('data-za-extra-module="')[1:]]
        elif a=='zvideos':
            h=[{'data-zop':eval(dehtml(c.split('"')[0]))}for c in h.split('data-zop="')[1:]]
        elif a=='answers':
            h=[{'data-zop':eval(dehtml(c.split('"')[0])),'link':'https://www.zhihu.com/question/%s'%c.split('//www.zhihu.com/question/')[1].split('"')[0]}for c in h.split('data-zop="')[1:]]
        else:raise TypeError
        h2=[]
        for c in range(len(h)):h2.append(h[len(h)-1-c])
        h=h2
        f=open(ed,'w+');f.write(repr(h));f.close()
        print(h)
