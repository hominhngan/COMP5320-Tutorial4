"""Lab 3: Add to cart browser test.

A shopper adds one Sauce Labs Backpack and verifies it in Your Cart.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_add_backpack_to_cart(driver):
    """Log in, add Sauce Labs Backpack, open cart, and verify product and quantity."""
    # Step 1: Log in with standard_user credentials
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page title
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-test="title"]'), "Products")
    )

    # Step 2: Add Sauce Labs Backpack to cart
    add_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]'))
    )
    add_btn.click()

    # Step 3: Open shopping cart
    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]'))
    )
    cart_link.click()

    # Step 4: Verify Your Cart page contents
    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-test="title"]'), "Your Cart")
    )
    cart_title = driver.find_element(By.CSS_SELECTOR, '[data-test="title"]')
    assert cart_title.text == "Your Cart"

    cart_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-test="inventory-item"]'))
    )
    assert len(cart_items) == 1

    product_name = cart_items[0].find_element(By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    assert product_name.text == "Sauce Labs Backpack"

    item_quantity = cart_items[0].find_element(By.CSS_SELECTOR, '[data-test="item-quantity"]')
    assert item_quantity.text == "1"
