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
driver.find_element("name", "email").send_keys("email")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
myele = driver.find_element("xpath", "//span[contains(.,'Signup Now')]")
print(myele.text)
myele.click()
time.sleep(1)
signups = [{"name": "Rajas", "email": "rajas@gmail.com", "phone": "9969342104", "password": "password", "agreeTerms": True}]
for i in signups:
    driver.find_element_by_name("name").send_keys(i["name"])
    driver.find_element_by_name("email").send_keys(i["email"])
    driver.find_element_by_name("phone").send_keys(i["phone"])
    driver.find_element_by_name("password").send_keys(i["password"])
    driver.find_element_by_name("agreeTerms").send_keys(i["agreeTerms"])
driver.close()  
print("sample test case successfully completed")  