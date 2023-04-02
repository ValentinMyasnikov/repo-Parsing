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
import time

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://mail.yandex.ru/')
button = driver.find_element(By.XPATH, '//a[@href="https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fmail.yandex.ru"]')
button.click()
time.sleep(1)
element_login = driver.find_element(By.ID, 'passp-field-login')
element_login.send_keys('*********') # вместо звездочек введите логин
button_sign = driver.find_element(By.XPATH, '//button[@data-t="button:action:passp:sign-in"]')
button_sign.click()
time.sleep(1)
element_passwd = driver.find_element(By.XPATH, '//input[@data-t="field:input-passwd"]')
element_passwd.send_keys('**********')  # вместо звездочек введите пароль
element_passwd.send_keys(Keys.ENTER)
time.sleep(5)
element_close = driver.find_element(By.XPATH, '//div[@class="BrokenCollectorWizard-m__closeButton--d3hrc qa-LeftColumn-BrokenCollectorWizard-Close"]')
element_close.click()
ya_mail_list = []
mails = driver.find_elements(By.XPATH, '//div[@class="ns-view-container-desc mail-MessagesList js-messages-list"]/div')


n=0

for m in mails:
    n += 1
    time.sleep(1)
    element_mail = m.find_element(By.XPATH, './/span[@class="mail-MessageSnippet-FromText"]')
    element_mail.click()
    time.sleep(2)
    sender_name = driver.find_element(By.XPATH, './/button[@class="Button2 Button2_size_s Button2_view_clear SenderName_sender_F3wYv undefined Sender_senderName_BQ7TB qa-MessageViewer-SenderName"]').text
    date = driver.find_element(By.XPATH, './/a[@class="Header_dateLink_Y2p9n qa-MessageViewer-Header-dateLink"]').text
    sender_mail = driver.find_element(By.XPATH, './/span[@class="Sender_email_iWFMG qa-MessageViewer-SenderEmail"]').text
    theme = driver.find_element(By.XPATH, './/span[@class="Text Text_color_primary Text_typography_subheader-m Title_subject_tyZv5"]').text
    #print(sender_name, sender_mail, date)
    element_back = driver.find_element(By.XPATH, './/div[@class="Folder-m__root--iLgY8 qa-LeftColumn-Folder Folder-m__selected--QRoPQ qa-LeftColumn-Folder_selected"]')
    element_back.click()
    mail_dict = {
    'sender_name': sender_name,
    'sender_mail': sender_mail,
    'date': date,
    'theme':theme
    }
    ya_mail_list.append(mail_dict)
    if n == 10:
        break

print(ya_mail_list) 
print()