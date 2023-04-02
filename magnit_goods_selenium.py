from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://magnit.ru/')
button = driver.find_element(By.XPATH, '//div[@class="header__nav-group header__nav-visible"]/a')
button.click()
button_age = driver.find_elements(By.XPATH, '//div[@class="confirm_age__answer"]/button')[1]
button_age.click()

for i in range(2):
    try:
        sale_goods = driver.find_element(By.XPATH, '//div[@class="catalogue__loading js-promo-load-more"]')
        actions = ActionChains(driver)
        actions.move_to_element(sale_goods)
        actions.perform()
    except NoSuchElementException:
        print('Список товаров окончен')
        break

magnit_sales = []
goods = driver.find_elements(By.XPATH, '//a[@class="card-sale card-sale_catalogue "]')
for g in goods:
    name_vol = g.find_element(By.XPATH, './/div[@class="card-sale__title"]/p').text
    sale = g.find_element(By.XPATH, './/div[@class="card-sale__col card-sale__col_img"]/div').text
    sale_type = g.find_element(By.XPATH, './/div[@class="card-sale__header"]').text
    news_dict = {
    'name_vol': name_vol,
    'sale': sale,
    'sale_type': sale_type
    }
    magnit_sales.append(news_dict)

print(magnit_sales)
with open('D:/Программки/Обучение в GB/Selenium/data_magnit_selenium.json', 'w') as outfile:
    json.dump(magnit_sales, outfile)

print()