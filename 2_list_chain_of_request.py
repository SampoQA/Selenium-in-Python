import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get("https://demoqa.com/menu")

# Исправленные локаторы:
MAIN_ITEM_2 = (By.XPATH, "//a[text()='Main Item 2']")  # Ищем по тексту элемента
SUB_SUB_LIST = (By.XPATH, "//a[text()='SUB SUB LIST »']")  # Учитываем полный текст

# Наводим на Main Item 2
main_item = driver.find_element(*MAIN_ITEM_2)
action.move_to_element(main_item).perform()

# Ожидаем появления выпадающего меню и находим SUB SUB LIST
wait = WebDriverWait(driver, 10)
sub_sub_item = wait.until(EC.visibility_of_element_located(SUB_SUB_LIST))

# Наводим на появившийся элемент
action.move_to_element(sub_sub_item).pause(3).perform()

time.sleep(2)
driver.quit()