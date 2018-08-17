# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 08:39:38 2018

@author: yinchao
"""


import re
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def GetPoetry(name):
    '''
    从古诗词网上爬去匹配的诗词，并返回第一篇内容
    '''
    url = 'https://so.gushiwen.org/search.aspx?value='
    url += name
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
    html = ''
    try:
        response = requests.get(url,headers = headers)                  
    #    response.encoding = 'utf-8'                        #解决中文乱码
        if response.status_code == 200:                     #判断是否爬取网页成功
            html = response.text
        else:
            return
    except RequestException:
        return 
    soup = BeautifulSoup(html,'html5lib')
    lls = soup.select('table#BalanceSheetNewTable0 tbody tr td')
    lls = soup.select('textarea')
#    print(lls[0])          
    try:
        pattern = '(?<=>).*(?=https)'
        obj = re.compile(pattern)
        match = obj.findall(str(lls[0]))
    #    print(match[0])       
        return match[0]
    except:
        return 0


def get_magzine_url():
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

url = "https://magazinelib.com/all/visual-merchandising-and-retail-design-august-2018/"    
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
try:
    response = requests.get(url,headers = headers)                  
#    response.encoding = 'utf-8'                        #解决中文乱码
    if response.status_code == 200:                     #判断是否爬取网页成功
        html = response.text #get raw web page
        print(html)
#        obj = 'https://magazinelib.com/all/[^\"]+'
#        pattern = re.compile(obj)
#        match = pattern.findall(html)

except:
    pass

if __name__ == "__main__":
    print(GetPoetry('千树万树梨花开'))
#    s = get_magzine_url()
    