from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://facebook.com')
email = driver.find_element(By.XPATH,'.//*[@id="email"]')
email.send_keys('mail@address.com')
password = driver.find_element(By.XPATH,'.//*[@id="pass"]')
password.send_keys('password')

login = driver.find_element(By.XPATH,'.//*[@id="loginbutton"]')
login.click()

status = driver.find_element(By.XPATH,'.//*[@name="xhpc_message"]')
time.sleep(5)

status.send_keys('This is a test. Sent by Selenium Webdriver.')
time.sleep(5)
buttons = driver.find_elements_by_tag_name('button')
time.sleep(5)
for item in buttons:
	if item.text == 'Opublikuj':
		item.click()