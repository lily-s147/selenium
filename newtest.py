import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ya.ru")

element = driver.find_element(By.XPATH, "//input[@class='search3__input mini-suggest__input']")
element.send_keys("Hello world")

button = driver.find_element(By.XPATH, "//button[contains(text(),'Найти')]")
button.click()

s = driver.current_url
print(s)

time.sleep(10)

driver.quit()
