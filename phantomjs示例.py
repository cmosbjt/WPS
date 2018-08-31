from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="C:/phantomjs_2_1/bin/phantomjs.exe")
driver.get("www.baidu.com")
data = driver.title
print (data)