from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Login with locked_out_user
driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Verify error message
error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
assert "locked out" in error_msg.lower()

print("Q1 Passed: Error message verified successfully")

driver.quit()
