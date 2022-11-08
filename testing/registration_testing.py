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
myele.click()
time.sleep(1)
signups = [{"name": "Rajas", "email": "rajas@gmail.com", "phone": "9969342104", "password": "password", "agreeTerms": True, "result": ""}]
name = driver.find_element("name", "name")
email = driver.find_element("name", "email")
phone = driver.find_element("name", "phone")
password = driver.find_element("name", "password")
agreeTerms = driver.find_element("name", "agreeTerms")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
myele = driver.find_element("xpath", "//button[@class='rounded-filled-btn'][contains(., 'Sign Up')]")
for i in signups:
    time.sleep(1)
    name.clear()
    email.clear()
    phone.clear()
    password.clear()
    if agreeTerms.is_selected():
        agreeTerms.click()
    name.send_keys(i["name"])
    email.send_keys(i["email"])
    phone.send_keys(i["phone"])
    password.send_keys(i["password"])
    if i["agreeTerms"]:
        agreeTerms.click()
    myele.click()
    time.sleep(2)
    i["result"] = driver.find_element("id", "notistack-snackbar").text
    driver.find_element("css selector", ".SnackbarItem-action").find_element("tag name", "button").click()
    time.sleep(1)
print(signups)
driver.close()  
print("sample test case successfully completed")  