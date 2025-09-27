# Login with standard_user
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Reset App State
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "reset_sidebar_link").click()

# Add 3 items to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Checkout process
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()

# Verify product names and total price
items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
for item in items:
    print("Product:", item.text)

total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
print("Total Price:", total)

# Finish purchase
driver.find_element(By.ID, "finish").click()
success_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
assert "THANK YOU" in success_msg.upper()

print("Q2 Passed: Order completed successfully")

# Reset and Logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "reset_sidebar_link").click()
driver.find_element(By.ID, "logout_sidebar_link").click()

driver.quit()
