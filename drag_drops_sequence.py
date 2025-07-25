import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver)

# driver.get("https://the-internet.herokuapp.com/drag_and_drop")

# COLLUMN_A = ("xpath", "//div[@id='column-a']")
# COLLUMN_B = ("xpath", "//div[@id='column-b']")

# A = driver.find_element(*COLLUMN_A)
# B = driver.find_element(*COLLUMN_B)
# time.sleep(2)  # Wait for the page to load

# action.drag_and_drop(A, B).pause(3).perform()
# time.sleep(2)  # Wait to see the result of the drag and drop


#что делать если элемент дв который нужно перетянуть появляеться позже 
driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

GRID_ITEM = ("xpath", "(//div[@class='grid__item'])[3]")
SLIDEBAR_ITEM = ("xpath", "(//div[@class='drop-area__item'])[3]")
action.click_and_hold(driver.find_element(*GRID_ITEM)).pause(1.5).move_to_element(driver.find_element(*SLIDEBAR_ITEM)).pause(1).release().perform()
time.sleep(5)  # Wait to see the result of the drag and drop