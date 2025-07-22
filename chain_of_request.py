import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver) # Создаем обьект action

LEFT_CLICK_BUTTON = ("xpath", "//button[@id='leftClick']")

driver.get("https://testkru.com/Elements/Buttons")

left_button= driver.find_element(*LEFT_CLICK_BUTTON)

time.sleep(3)  # Задержка для наблюдения результата

action.click(left_button).perform()  # Важно использовать метод perform() для выполнения действия завершения цепочки действий

time.sleep(3)  # Задержка для наблюдения результата