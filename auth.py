# auth.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")

CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"

class TestLoginAuth:
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service, options=options)
        self.wait = WebDriverWait(self.driver, 10)
        logging.info("Браузер запущен успешно.")

    def open_login_page(self):
        logging.info("Открываю страницу логина...")
        self.driver.get("https://the-internet.herokuapp.com/login")
        logging.info("Страница логина открыта.")

    def login(self, username, password):
        try:
            logging.info("Ввожу логин...")
            self.wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
            
            logging.info("Ввожу пароль...")
            self.driver.find_element(By.ID, "password").send_keys(password)
            
            logging.info("Нажата кнопка Login.")
            self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()
            
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
            logging.info("Вход выполнен успешно!")
        except Exception as e:
            logging.error(f"Ошибка: {e}")

    def go_to_registration(self):
        logging.info("Переход на страницу регистрации (имитация)...")
        self.driver.get("https://the-internet.herokuapp.com/secure")
        logging.info("Страница 'регистрации' открыта (имитация).")

    def close(self, delay_seconds=5):
        logging.info(f"Жду {delay_seconds} секунд перед закрытием браузера...")
        time.sleep(delay_seconds)
        self.driver.quit()
        logging.info("Браузер закрыт.")
