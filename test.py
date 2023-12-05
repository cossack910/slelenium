from selenium import webdriver
import time

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
             command_executor = 'http://selenium:4444/wd/hub',
             options = options
             )

driver.implicitly_wait(10)

url = ''
driver.get(url)

time.sleep(3)
driver.save_screenshot('test.png')
driver.quit()

# docker exec -it python3 python test.py