# this code is working fine but it is not 100% accurate


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
import time

# driver = webdriver.Chrome("chromedriver",webdriver.ChromeOptions)  # Replace with the path to your chromedriver executable
driver = webdriver.Edge()

driver.get("https://erp.aktu.ac.in/webpages/oneview/oneview.aspx")
try:
    roll_number_input = driver.find_element("id","txtRollNo")
    roll_number_input.send_keys('2200970140075')
    proceed_button = driver.find_element("id",'btnProceed')
    proceed_button.click()
    dob_input = driver.find_element("id","txtDOB")
    dob_input.send_keys('02-07-2002')
    dob_input.send_keys(Keys.ENTER)

    # Solve the CAPTCHA manually or use a CAPTCHA solving service
    print(" all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go all set to go")
    captcha_iframe = driver.find_element(By.XPATH, '//*[@id="pnlCaptcha"]/span/div/div/div/iframe')
    driver.switch_to.frame(captcha_iframe)
    print(" captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found captche found")
    # captcha_input = driver.find_element(By.CLASS_NAME, 'rc-anchor-center-item')


    time.sleep(2)
    captcha_input = driver.find_element(By.ID, 'recaptcha-anchor-label')
    time.sleep(2)
    captcha_input.click()
    time.sleep(2)
    captcha_input.click()
    time.sleep(2)
    captcha_input.click()
    print("Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: Enter the captcha: ")

    # this will return to the website frame from the captcha frame
    driver.switch_to.default_content()
    # After solving the CAPTCHA, click the submit button

    submit_button = driver.find_element("id",'btnSearch')
    submit_button.click()
    # Wait for a specific element on the result page to load (e.g., a result table)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.result-table')))
    # Get the result table
    result_table = driver.find_element_by_css_selector('table.result-table')


except Exception as e:
    print(e , "error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error-error")
    driver.quit()