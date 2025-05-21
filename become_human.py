import time
from selenium import webdriver # Импортируем "пульт управления" для браузера (основной инструмент Selenium)
from webdriver_manager.chrome import ChromeDriverManager # Импортируем "автопомощника" для автоматической установки Chrome-драйвера
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # Импортируем "инструкцию по запуску" для настройки Chrome-драйвера
from selenium.webdriver.support.ui import WebDriverWait #драйвер явного ожидания
from selenium.webdriver.support import expected_conditions as EC #какие условия ожидаем. as EC позволяет писать EC вместо expected_conditions

options = Options() #создаёт объект, который обычно используется для настройки поведения браузера
options.add_argument("--headless") # поднять без внешнего проявления
#options.add_argument("--window-size=1920,1080") # размеры окна 
options.add_argument("--disable-blink-features=AutomationControlled") # скрыть что это алгоритм, а не человек
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36") #юзерские показатели открывателя браузера

service = Service(ChromeDriverManager().install()) #Готовим "инструкцию" для драйвера, указывая где его взять: ChromeDriverManager сам найдет и скачает нужную версию драйвера
driver = webdriver.Chrome(service=service, options=options) # Заводим "машину" (браузер Chrome) с нашей инструкцией driver - наш "руль" для управления браузером
wait = WebDriverWait(driver, 5, poll_frequency=1) #создает объект явного ожидания 5 это максимальное время ожидания в сек. poll_frequency=1: проверяет условие выполнено кажд 1 сек

driver.get("https://whatismyipaddress.com/") #ссылка на сайт

wait.until(EC.title_is("What Is My IP Address - See Your Public Address - IPv4 & IPv6")) #ждём появление тайтла

driver.save_screenshot("screen.png") #делаем скриин того что получиться без видимого отображения браузера 


