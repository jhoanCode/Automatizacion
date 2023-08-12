from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

# driver_path = 'C:\\Users\\Jhoan\\Downloads\\chromedriver_win32\\chromedriver.exe'
# driver_path, chrome_options=options

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.accuweather.com/')


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.banner-button.policy-accept')))\
    .click()
driver.save_screenshot('captura1.png')

time.sleep(2)


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.search-input')))\
    .send_keys('santo Domingo')
driver.save_screenshot('captura2.png')

time.sleep(3)


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'svg.search-icon')))\
    .click()
driver.save_screenshot('captura3.png')

time.sleep(4)


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'svg.hamburger-button.icon-hamburger')))\
    .click()
driver.save_screenshot('captura4.png')

time.sleep(5)


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'a.header-link')))\
    .click()
driver.save_screenshot('captura5.png')

time.sleep(10)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.forecast-container')))\
    .click()
driver.save_screenshot('captura6.png')

time.sleep(7)

