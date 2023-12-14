import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from captcha_bypass import solve_captcha

def bypass_captcha(driver):
    ########################################################
    

    #######################################################
    # Find the captcha element.
    # captcha_element = driver.find_element("id","g-recaptcha-response")

    # # Create an ActionChains object.
    # action_chains = ActionChains(driver)

    # # Move the mouse to the captcha element.
    # action_chains.move_to_element(captcha_element)

    # # Click the captcha element.
    # action_chains.click(captcha_element)

    # # Release the mouse button.
    # action_chains.release()

    # # Perform the action chains.
    # action_chains.perform()

    captcha_div = driver.find_element(By.ID, "g-recaptcha-response")
 
    driver.switch_to.frame(captcha_div.find_element(By.TAG_NAME, "iframe"))
 
    checkbox = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-checkmark")
    checkbox.click() 
    driver.switch_to.default_content()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    browser.get("https://www.google.com/recaptcha/api2/demo")
    # Filter through all the iframes on the page and find the one that corresponds to the captcha
    # iframes = browser.find_elements_by_tag_name("iframe")
    iframes = driver.find_element("id","g-recaptcha-response")
    for iframe in iframes:
        if iframe.get_attribute("src").startswith("https://www.google.com/recaptcha/api2/anchor"):
            captcha = iframe
    solve_captcha(browser, iframes)



# recaptcha-token


































































































def login(driver, username, password):
    # Find the username field.
    username_field = driver.find_element("id","txtRollNo")

    # Enter the username.
    username_field.send_keys(username)

    # Find the proceed button.
    proceed_button = driver.find_element("id","btnProceed")

    # Click the proceed button.
    proceed_button.click()

    # Find the password field.
    password_field = driver.find_element("id", "txtDOB")

    # Enter the password.
    password_field.send_keys(password)

    print("Solving captcha...")
    # Bypass the captcha.
    bypass_captcha(driver)
    print("Done")
    # Find the login button.
    login_button = driver.find_element("id","btnSearch")

    # Click the login button.
    login_button.click()

def main():
    # Create a new Selenium WebDriver instance.
    driver = webdriver.Chrome()
    print("Opening website...")
    # Open the website.
    driver.get('https://erp.aktu.ac.in/webpages/oneview/oneview.aspx')

    # Login to the website.
    login(driver, '2200970140075', '02-07-2002')

    # Close the WebDriver instance.
    # driver.quit()
    print("Done")

if __name__ == '__main__':
    main()