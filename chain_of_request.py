import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver) # Создаем обьект action

LEFT_CLICK_BUTTON = ("xpath", "//button[@id='leftClick']")
DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClick']")
RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClick']")
HOVER_BUTTON = ("xpath", "//button[@id='colorChangeOnHover']")

driver.get("https://testkru.com/Elements/Buttons")

left_button= driver.find_element(*LEFT_CLICK_BUTTON)
double_button = driver.find_element(*DOUBLE_CLICK_BUTTON)
right_button = driver.find_element(*RIGHT_CLICK_BUTTON)
hover_button = driver.find_element(*HOVER_BUTTON)

time.sleep(3)  # Задержка для наблюдения результата
action.click(left_button).pause(3).double_click(double_button).context_click(right_button).perform()  # Цепочка действий

# action.double_click(double_button).perform()  # Двойной клик по кнопке
# time.sleep(5)  # Задержка для наблюдения результата

# action.context_click(right_button).perform()  # Правый клик по кнопке
# time.sleep(5)  # Задержка для наблюдения результата

# action.click(left_button).perform()  # Левый клик по кнопке
time.sleep(5)  # Задержка для наблюдения результата
action.move_to_element(hover_button).perform()  # Наведение курсора на кнопку
time.sleep(5)  # Задержка для наблюдения результата