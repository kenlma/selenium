import time
from selenium import webdriver

driver = webdriver.PhantomJS(service_log_path='/var/log/phantomjs/ghostdriver.log')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
#time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
print (driver.current_url)
time.sleep(5) # Let the user actually see something!
driver.quit()