from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

try:
    # Login
    driver.get("https://oneui-phtwo.canvas.cellcard.com.kh/")
    print("Title is:", driver.title)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("keanu")
    driver.find_element(By.ID, "password").send_keys("keanu@123", Keys.RETURN)
    time.sleep(5)

    # Navigate to Teams
    driver.get("https://oneui-phtwo.canvas.cellcard.com.kh/#/team")

    # Click "Add Team"
    add_team_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add Team')]")))
    driver.execute_script("arguments[0].click();", add_team_btn)

    # Wait for modal-body to appear anywhere in DOM
    modal_body = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.modal-body")))

    # Locate input inside modal
    team_input = modal_body.find_element(By.XPATH, ".//input[@placeholder='Team Name']")

    # Generate 4-digit unique team name
    unique_team_name = f"Automata{str(int(time.time()))[-4:]}"
    driver.execute_script("""
        arguments[0].value = arguments[1];
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, team_input, unique_team_name)

    # Wait for Submit button to become enabled
    submit_btn = None
    for _ in range(30):  # up to 15 seconds
        try:
            submit_btn = modal_body.find_element(By.XPATH, ".//button[contains(text(),'Submit')]")
            if submit_btn.is_enabled():
                break
        except:
            pass
        time.sleep(0.5)
    else:
        raise Exception("Submit button never became enabled!")

    # Click Submit
    driver.execute_script("arguments[0].click();", submit_btn)
    print(f"Clicked Submit successfully for team: {unique_team_name}")

    time.sleep(5)

finally:
    driver.quit()
