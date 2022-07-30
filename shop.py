import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)

# maximize window
driver.maximize_window()

#login
driver.get("https://practice.automationtesting.in/")

#click my Account
account = driver.find_element_by_css_selector("#menu-item-50 > a")
time.sleep(1)
account.click()

username = driver.find_element_by_id("username")
username.send_keys("test-auto-3007@test.com")

password = driver.find_element_by_id("password")
password.send_keys("test-auto-3007")

btn_login = driver.find_element_by_css_selector("input[value='Login']")
btn_login.click()

#click Shop
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#click book
book = driver.find_element_by_xpath("//h3[text()='HTML5 Forms']")
book.click()

#check book header name
book_header = driver.find_element_by_css_selector("h1[itemprop='name']")
assert 'HTML5 Forms' in book_header.text

driver.quit()

#login
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://practice.automationtesting.in/")

#click my Account
account = driver.find_element_by_css_selector("#menu-item-50 > a")
time.sleep(1)
account.click()

username = driver.find_element_by_id("username")
username.send_keys("test-auto-3007@test.com")

password = driver.find_element_by_id("password")
password.send_keys("test-auto-3007")

btn_login = driver.find_element_by_css_selector("input[value='Login']")
btn_login.click()

#click to shop
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#click HTML
html =driver.find_element_by_css_selector("ul.product-categories > li:nth-child(2) > a")
html.click()

#check for product qty
products = driver.find_elements_by_xpath("//a[text()='Add to basket']")
assert len(products) == 3

driver.quit()

# _____________________________________________________
# CHECK SELECT
#
# login
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://practice.automationtesting.in/")

# maximize window
driver.maximize_window()

#click my Account
account = driver.find_element_by_css_selector("#menu-item-50 > a")
time.sleep(1)
account.click()

username = driver.find_element_by_id("username")
username.send_keys("test-auto-3007@test.com")

password = driver.find_element_by_id("password")
password.send_keys("test-auto-3007")

btn_login = driver.find_element_by_css_selector("input[value='Login']")
btn_login.click()

#click to shop
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#check select for default
default = driver.find_element_by_css_selector(".orderby > option[selected='selected']").get_attribute("value")
assert 'menu_order' in default

#sort product by desc
selector = driver.find_element_by_css_selector(".orderby")
select = Select(selector)
price_desc = select.select_by_value("price-desc")

#check for selector value
selected = driver.find_element_by_css_selector(".orderby > option[selected='selected']").get_attribute("value")
assert 'price-desc' in selected

driver.quit()

# _____________________________________________________
# CHECK BOOK PRICE

#login
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://practice.automationtesting.in/")

# maximize window
driver.maximize_window()

#click my Account
account = driver.find_element_by_css_selector("#menu-item-50 > a")
time.sleep(1)
account.click()

username = driver.find_element_by_id("username")
username.send_keys("test-auto-3007@test.com")

password = driver.find_element_by_id("password")
password.send_keys("test-auto-3007")

btn_login = driver.find_element_by_css_selector("input[value='Login']")
btn_login.click()

#click to shop
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#click selenium Android book
book = driver.find_element_by_xpath("//h3[text()='Android Quick Start Guide']")
book.click()

#check for old/new price
old = driver.find_element_by_css_selector("del > span")
assert old.text == '₹600.00'
new = driver.find_element_by_css_selector("ins > span")
assert new.text == '₹450.00'


#check preview modal
img = driver.find_element_by_css_selector("a[itemprop='image']")
img.click()

img_preview = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.ID, "fullResImage")))

#close preview modal
btn_close = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")))
btn_close.click()

driver.quit()


# _____________________________________________________
# CHECK PRICE IN CART

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://practice.automationtesting.in/")

# maximize window
driver.maximize_window()

#click to shop
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
time.sleep(1)
shop.click()

#add to cart HTML5 book
book = driver.find_element_by_css_selector("a[data-product_id='182']")
book.click()
time.sleep(2)

#check for cart item qty & price
item = WebDriverWait(driver, 3).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.cartcontents"), 'Item'))
item_qty = driver.find_element_by_css_selector("span.cartcontents")
assert item_qty.text == '1 Item'
item_price = driver.find_element_by_css_selector("span.amount")
assert item_price.text == '₹180.00'

#go to cart
cart = driver.find_element_by_css_selector("a.wpmenucart-contents")
cart.click()

#check totals
sub_total = WebDriverWait(driver, 2).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td[data-title='Subtotal'] > span"), '₹180.00'))

total = WebDriverWait(driver, 2).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td[data-title='Total'] > strong > span"), '₹183.60'))
driver.quit()

# _____________________________________________________
# ADD TWO BOOKS IN CART AND CHECK QTY

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://practice.automationtesting.in/")

# maximize window
driver.maximize_window()

#click to shop
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
time.sleep(1)
shop.click()

# scroll down 300
driver.execute_script("window.scrollBy(0, 300);")

#add to cart HTML5 book
book_one = driver.find_element_by_css_selector("a[data-product_id='182']")
book_one.click()
time.sleep(2)

#add to cart JS book
book_two = driver.find_element_by_css_selector("a[data-product_id='180']")
book_two.click()
time.sleep(1)

#go to cart
cart = driver.find_element_by_css_selector("a.wpmenucart-contents")
cart.click()
time.sleep(1)

#delete book from cart
book_one_delete = driver.find_element_by_css_selector("a[data-product_id='182']")
book_one_delete.click()
time.sleep(1)

#undo deleted book
undo = driver.find_element_by_css_selector(".woocommerce-message > a")
undo.click()

#change qty
qty = driver.find_element_by_css_selector("tbody > .cart_item > .product-quantity input")
qty.clear()
qty.send_keys(3)

#update basket
btn_update_basket = driver.find_element_by_css_selector("input[name='update_cart']")
btn_update_basket.click()

#check qty
qty = driver.find_element_by_css_selector("tbody > .cart_item > .product-quantity input")
qty_value = qty.get_attribute("value")
assert qty_value == '3'

#apply coupon
time.sleep(1)
btn_apply_coupon = driver.find_element_by_css_selector("input[name='apply_coupon']")
btn_apply_coupon.click()

#check coupon text message
message = driver.find_element_by_css_selector(".woocommerce-error > li")
assert message.text == 'Please enter a coupon code.'

driver.quit()


# _____________________________________________________
#ADD TWO BOOKS IN CART AND CHECK QTY

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://practice.automationtesting.in/")

# maximize window
driver.maximize_window()

#click to shop
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
time.sleep(1)
shop.click()

# scroll down 300
driver.execute_script("window.scrollBy(0, 300);")

#add to cart HTML5 book
book_one = driver.find_element_by_css_selector("a[data-product_id='182']")
book_one.click()
time.sleep(2)

#go to cart
cart = driver.find_element_by_css_selector("a.wpmenucart-contents")
cart.click()
time.sleep(1)

#click checkout
checkout = WebDriverWait(driver, 2).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout > a")))
checkout.click()

#fill billing form
first_name = WebDriverWait(driver, 2).until(
     EC.visibility_of_element_located((By.ID, "billing_first_name")))
first_name.send_keys("bookbuyer")

last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("bookbuyer")

email = driver.find_element_by_id("billing_email")
email.send_keys("test-auto-3007@test.com")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("12345678")

country_selector = driver.find_element_by_xpath("//div[contains(@class, 'select2-container')]")
country_selector.click()
time.sleep(1)

country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("russia")

country_search_match = driver.find_element_by_css_selector("span.select2-match")
country_search_match.click()

address = driver.find_element_by_id("billing_address_1")
address.send_keys("book buyer main street")

city = driver.find_element_by_id("billing_city")
city.send_keys('spb')

state = driver.find_element_by_id("billing_state")
state.send_keys('spb')

zip_code = driver.find_element_by_id("billing_postcode")
zip_code.send_keys("123456")

# scroll down 600
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)

#select Check Payments
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()
time.sleep(2)

#place order
btn_place_order = driver.find_element_by_id("place_order")
btn_place_order.click()

#check order text
text = WebDriverWait(driver, 2).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), 'Thank you. Your order has been received.'))

#check for payment method
paument = WebDriverWait(driver, 2).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.method > strong"), 'Check Payments'))

driver.quit()
