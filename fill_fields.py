import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

full_name = driver.find_element("xpath", "//*[@id='userName']")
full_name.clear()
assert full_name.get_attribute("value") == ""
full_name.send_keys("Chack Ivanovich li") 
assert full_name.get_attribute("value") == "Chack Ivanovich li"

user_email = driver.find_element("xpath", "//*[@id='userEmail']")
user_email.clear()
assert user_email.get_attribute("value") == ""
user_email.send_keys("test@test.com")

current_address = driver.find_element("xpath", "//*[@id='currentAddress']")
current_address.clear()
assert current_address.get_attribute("value") == ""
current_address.send_keys("isoisälle kylään")
assert current_address.get_attribute("value") == "isoisälle kylään"

permanent_address = driver.find_element("xpath","//*[@id='permanentAddress']")
permanent_address.clear()
assert permanent_address.get_attribute("value") == ""
permanent_address.send_keys("London, Baker Street 22b")
assert permanent_address.get_attribute("value") == "London, Baker Street 22b"

button_submit = driver.find_element("xpath","//*[@id='submit']")
button_submit.click()

time.sleep(3)
