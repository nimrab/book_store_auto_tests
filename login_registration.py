import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(3)

# maximize window
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")

#click my Account
account = driver.find_element_by_css_selector("#menu-item-50 > a")
time.sleep(1)
account.click()

#register
email = driver.find_element_by_id("reg_email")
email.send_keys("test-auto-3007@test.com")

password = driver.find_element_by_id("reg_password")
password.send_keys("test-auto-3007")
time.sleep(1)

#click to empty space
header = driver.find_element_by_xpath("//h2[text()='Register']")
header.click()


#wait for password power response
btn_register = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Register']")))

btn_register.click()

driver.quit()


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

#check if Logout text availibe

logout = driver.find_element_by_css_selector("nav.woocommerce-MyAccount-navigation > ul > li:nth-child(6) > a")
assert 'Logout' in logout.text

driver.quit()