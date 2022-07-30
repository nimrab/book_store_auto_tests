import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)

# maximize window
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")

# scroll down 600
driver.execute_script("window.scrollBy(0, 600);")

#click selenium ruby book
book = driver.find_element_by_xpath("//h3[text()='Selenium Ruby']")
time.sleep(1)
book.click()

#click reviews
reviews = driver.find_element_by_css_selector(".tabs.wc-tabs > li:nth-child(2) > a")
reviews.click()

#click 5 star rating
rating = driver.find_element_by_css_selector(".star-5")
rating.click()

#leave comment
textarea = driver.find_element_by_id("comment")
textarea.send_keys("Nice book!")

name = driver.find_element_by_id("author")
name.send_keys("good man")

email = driver.find_element_by_id("email")
email.send_keys("goodman@test.com")

submit = driver.find_element_by_id("submit")
submit.click()

driver.quit()