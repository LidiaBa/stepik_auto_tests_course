from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math








def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
  

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    # Ваш код, который заполняет обязательные поля
    
    input1 = browser.find_element(By.ID, 'answer')
    browser.execute_script("window.scrollBy(0, 100);", input1) 
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()