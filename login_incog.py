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
uname = driver.find_element(By.ID, "username")
uname.send_keys("keanu")

# --- Fill Password ---
passw = driver.find_element(By.ID, "password")  # replace if different
passw.send_keys("keanu@123")

# --- Press Enter to Submit ---
passw.send_keys(Keys.RETURN)

# Optional: wait to see what happens
time.sleep(15)

driver.quit()