import time
from selenium import webdriver # Импортируем "пульт управления" для браузера (основной инструмент Selenium)
from webdriver_manager.chrome import ChromeDriverManager # Импортируем "автопомощника" для автоматической установки Chrome-драйвера
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # Импортируем "инструкцию по запуску" для настройки Chrome-драйвера
from selenium.webdriver.support.ui import WebDriverWait #драйвер явного ожидания
from selenium.webdriver.support import expected_conditions as EC #какие условия ожидаем. as EC позволяет писать EC вместо expected_conditions

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install()) #Готовим "инструкцию" для драйвера, указывая где его взять: ChromeDriverManager сам найдет и скачает нужную версию драйвера
driver = webdriver.Chrome(service=service, options=options) # Заводим "машину" (браузер Chrome) с нашей инструкцией driver - наш "руль" для управления браузером
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://omayo.blogspot.com/")

driver.save_screenshot("screen.png")
