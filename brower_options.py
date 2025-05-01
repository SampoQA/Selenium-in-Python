import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal" #дефолтная можне не указывать слово "normal", ждёт всей загрузки страницы, всех ресурсов
chrome_options.page_load_strategy = "eager" #не ждёт всей загрузки страницы, всех ресурсов


# chrome_options.page_load_strategy = "normal"
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1700,1700") #фиксируйте размер окна, в докере в контейнере его не видно размер 
# chrome_options.add_argument("--disble-cash")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options) #переброс опций сюда важен

driver.set_window_size(1920, 1080) #сначала иниилизирует дравер открывает дефолтный размер окна , а потом выставляет нужный размер
start_time = time.time() #начало времени загрузки 

driver.get("https://whatismyipaddress.com/api")
#driver.get("https://expired.badssl.com/")

end_time = time.time() # конец времени загрузки

result_time = end_time - start_time #количества времени на загрузку страницы

print(result_time) #вывод времени normal 1.0638844966888428 eager 0.16231369972229004
