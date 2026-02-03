from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from os import getcwd
from os.path import join
import time


# Set up webdriver
driver_option = webdriver.ChromeOptions()
driver_option.add_argument("-incognito")
driver_path = join(getcwd(), "utilities", "webdrivers", "chromedriver-win64", "chromedriver.exe")
print(driver_path)
driver_service = Service(executable_path=driver_path)

def createWebDriver():
    return webdriver.Chrome(service=driver_service, options=driver_option)

# Open realtyworld website
browser = createWebDriver()
browser.get("https://realtyworld.com.mx")
time.sleep(10) # --DEBUG TODO: Add only if debug flag is active

# Close browser
browser.quit()