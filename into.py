from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://oneui-phtwo.canvas.cellcard.com.kh/")
print(driver.title)
driver.quit()