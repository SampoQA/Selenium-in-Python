import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Указываем путь для загрузки файлов (вариант для Windows)
download_dir = f"{os.getcwd()}\\downloads"  # Два обратных слеша для Windows

chrome_options = webdriver.ChromeOptions()

# Настройки для автоматической загрузки
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False  # Отключаем диалоговое окно
}
chrome_options.add_experimental_option("prefs", prefs)

# Фиксируем размер окна
chrome_options.add_argument("--window-size=1700,1700")

# Инициализация драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открываем страницу
driver.get("https://the-internet.herokuapp.com/download")
time.sleep(3)

# Находим все ссылки для скачивания
links = driver.find_elements("xpath", "//div[@class='example']//a")

# Скачиваем файлы
for link in links:
    link.click()
    time.sleep(1)  # Пауза между кликами

# Завершение работы
time.sleep(10)  # Ожидание завершения загрузок
driver.quit()