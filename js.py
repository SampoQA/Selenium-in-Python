import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls


driver = webdriver.Chrome()
action = ActionChains(driver)
scrols = Scrolls(driver, action)

driver.get("https:/seiyria.com/bootstrap-slider/")

# driver.execute_script("alert('Hello, world!')")# This will trigger an alert in the browser
EX_2_LOCATOR = ("xpath", "//h3[text()='Example 2:']")
EX_2 = driver.find_element(*EX_2_LOCATOR)

# action.scroll_to_element(EX_2).pause(4).perform() # Scroll to the Example 2 section WITHOT SCROLLS
scrolls.scroll_to_element(EX_2)  # Scroll to the Example 2 section WITH SCROLLS

time.sleep(5)
