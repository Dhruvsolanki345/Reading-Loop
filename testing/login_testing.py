from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
# driver = webdriver.Chrome("C:/Users/Rajas/chromedriver_win32/chromedriver.exe")
ser = Service("C:/Users/Rajas/geckodriver_win32/geckodriver.exe")
# driver = webdriver.Firefox(executable_path= "C:/Users/Rajas/geckodriver_win32/geckodriver.exe")
op = webdriver.FirefoxOptions()

options = Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

driver = webdriver.Firefox(service=ser, options=options)
print("Registration test case started")  
driver.get("https://reading-loop-528f8.web.app/login")
driver.maximize_window()  
time.sleep(2)
signups = [{"email": "rajas.bondale@somaiya.edu", "password": "Kk4GLcjLT5mUbdX"}]
for i in signups:
    driver.find_element("name", "email").send_keys(i["email"])
    driver.find_element("name", "password").send_keys(i["password"])
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
myele = driver.find_element("xpath", "//button[@class='rounded-filled-btn'][contains(., 'Login')]")
# myele.click()
driver.close()  
print("sample test case successfully completed")  