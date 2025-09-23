from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")   # <-- This enables Incognito mode

# Launch Chrome with options
driver = webdriver.Chrome(options=options)
driver.get("https://oneui-phtwo.canvas.cellcard.com.kh")
print("Page Title:", driver.title)

# --- Fill Username ---
driver.find_element(By.ID, "username").send_keys("keanu")

# --- Fill Password ---
driver.find_element(By.ID, "password").send_keys("keanu@123",Keys.RETURN)

# --- Press Enter to Submit ---

time.sleep(30)

driver.quit()