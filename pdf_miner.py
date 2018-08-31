import requests
file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
 
url = 'http://www.jac.com.cn/u/cms/www/201712/1511064206fz.pdf'   
#url = 'https://vk.com/doc423424436_474371004?hash=34b16dc9b0a200fe2b&amp;dl=GQ4TONRUGAZTG:1535535812:49926ab76331c31caf&amp;api=1&amp;no_preview=1'

r = requests.get(url, stream = True)
with open("python.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
 
         # writing one chunk at a time to pdf file
         if chunk:
             pdf.write(chunk)