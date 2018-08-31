# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 08:39:38 2018

@author: yinchao
"""


import re
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from selenium import webdriver

def get_magzine_url():
    '''
    从主页上拉取最新的杂志链接地址
    返回值：
    成功： 以list的形式返回所有更新链接
    失败： 返回-1或者0
    '''
    url = 'https://magazinelib.com/'    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
    try:
        response = requests.get(url,headers = headers)                  
    #    response.encoding = 'utf-8'                        #解决中文乱码
        if response.status_code == 200:                     #判断是否爬取网页成功
            html = response.text #get raw web page
            obj = 'https://magazinelib.com/all/[^\"]+'
            pattern = re.compile(obj)
            match = pattern.findall(html)
            return list(set(match))
        else:
            return 0
    except:
        return -1


def get_pdf_url(url):
    '''
    根据主页的链接地址来获取pdf的网址
    成功：返回 pdf的名称
    失败：返回 -1或者-2
    '''
    obj = webdriver.PhantomJS(executable_path="C:/phantomjs_2_1/bin/phantomjs.exe")
    try:
        obj.set_page_load_timeout(5)
        obj.get(url)
        obj.implicitly_wait(10)
        head_name = obj.title #得到杂志的名称
        html = obj.page_source
        pattern = r'(?<=\"vk-att-item\"><a href=\")([^\"]+)'
        obj = re.compile(pattern)
        match = obj.findall(html)
        if len(match):
#            print(match[0])
    #        obj.quit() 
            return match[0], head_name
        else:
            return -2
    except Exception as e:
        print(e)
        return -1

url = 'http://www.jac.com.cn/u/cms/www/201712/1511064206fz.pdf'   
def download_pdf(url, file_name):
    '''
    从指定的url地址下载pdf文件，并保存为file_name.pdf
    '''
    r = requests.get(url, stream = True)
    with open(file_name+'.pdf',"wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
             if chunk:
                 pdf.write(chunk)
        
    
if __name__ == "__main__":
    s = get_magzine_url()
    print(len(s))
    cnt = 0
    for url in s:
       cnt = cnt+1
       if cnt > 3:
           break
       pdf_url, pdf_head = get_pdf_url(url)
       if pdf_url == -2 or pdf_url == -1:
           print('cannot get this pdf_url')
           continue
       download_pdf(pdf_url, pdf_head)