from selenium import webdriver
from selenium.webdriver.common.by import By as By
from selenium.webdriver.common.keys import Keys as Keys


driver=webdriver.Chrome()
driver.get("https://oneui-phtwo.canvas.cellcard.com.kh")
print (driver.title)


# Find username input field by ID
username_field = driver.find_element(By.ID, "username")

# Print out some of its attributes
print("ID:", username_field.get_attribute("id"))
print("Name:", username_field.get_attribute("name"))
print("Type:", username_field.get_attribute("type"))
print("Class:", username_field.get_attribute("class"))


driver.quit()