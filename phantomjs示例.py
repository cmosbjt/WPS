from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="C:/phantomjs_2_1/bin/phantomjs.exe")
driver.get("https://www.geeksforgeeks.org/downloading-files-web-using-python/")
data = driver.title
print (data)