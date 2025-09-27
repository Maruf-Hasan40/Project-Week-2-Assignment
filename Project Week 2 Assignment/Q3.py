# Login with performance_glitch_user
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Reset App State
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "reset_sidebar_link").click()

# Filter Z to A
driver.find_element(By.CLASS_NAME, "product_sort_container").click()
driver.find_element(By.XPATH, "//option[@value='za']").click()

# Select first product
driver.find_element(By.CLASS_NAME, "btn_inventory").click()

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Checkout
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Alice")
driver.find_element(By.ID, "last-name").send_keys("Smith")
driver.find_element(By.ID, "postal-code").send_keys("54321")
driver.find_element(By.ID, "continue").click()

# Verify product and price
items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
for item in items:
    print("Product:", item.text)

total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
print("Total Price:", total)

# Finish purchase
driver.find_element(By.ID, "finish").click()
success_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
assert "THANK YOU" in success_msg.upper()

print("Q3 Passed: Order completed successfully")

# Reset and Logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "reset_sidebar_link").click()
driver.find_element(By.ID, "logout_sidebar_link").click()

driver.quit()
