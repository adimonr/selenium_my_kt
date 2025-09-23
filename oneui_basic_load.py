from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")   # <-- This enables Incognito mode

# Launch Chrome with options
driver = webdriver.Chrome(options=options)
driver.get("https://oneui-phtwo.canvas.cellcard.com.kh/")
print(driver.title)

driver.quit()   