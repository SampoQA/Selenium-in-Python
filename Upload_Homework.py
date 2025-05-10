import os  # Импорт модуля для работы с операционной системой (пути, директории)
import time  # Импорт модуля для работы со временем (задержки, ожидания)
from selenium import webdriver  # Импорт веб-драйвера Selenium для автоматизации браузера
from webdriver_manager.chrome import ChromeDriverManager  # Менеджер для автоматической установки ChromeDriver
from selenium.webdriver.chrome.service import Service  # Класс для управления сервисом ChromeDriver

chrome_options = webdriver.ChromeOptions() # Создаем объект-конфигуратор для управления настройками Chrome
service = Service(executable_path=ChromeDriverManager().install()) #  Создание сервиса для управления ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options) #Инициализация драйвера Chrome с настройками

chrome_options.add_argument("--window-size=1700,1700") #фиксируйте размер окна, в докере в контейнере его не видно размер 
driver.set_window_size(1920, 1080) 


driver.get("https://demoqa.com/upload-download")


time.sleep(3) #задержка 3 сек 

upload_file = driver.find_element("xpath","//*[@id='uploadFile']")
upload_file.send_keys(f"{os.getcwd()}\\downloads\\2025-05-05_16-34-06.png")

time.sleep(10) #задержка 10 сек 