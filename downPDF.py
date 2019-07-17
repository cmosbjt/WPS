# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:04:25 2018

@author: 54206
"""

from requests.exceptions import RequestException

import urllib

url = 'http://www.jac.com.cn/u/cms/www/201712/1511064206fz.pdf'
pdfname = 'test.pdf'
def getPDF(url,pfdName):
    pdf_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(pfdName, 'wb')
    
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + pdf_name)
    return pdf_name

getPDF(url,pdfname)
