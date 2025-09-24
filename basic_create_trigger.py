from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://oneui-phtwo.canvas.cellcard.com.kh/")
print("Title is", driver.title)
driver.find_element(By.ID, "username").send_keys("keanu")
driver.find_element(By.ID, "password").send_keys("keanu@123", Keys.RETURN)


time.sleep(10)

driver.get("https://oneui-phtwo.canvas.cellcard.com.kh/#/team")

driver.find_element(By.CSS_SELECTOR, "button.btn.btn-app-secondary.btn-submit").click()
time.sleep(3)
driver.find_element(By.ID, "Team Name").send_keys("Selenium Created User", Keys.RETURN)
time.sleep(20)
driver.quit()