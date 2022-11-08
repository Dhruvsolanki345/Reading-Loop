from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import pandas as pd
# driver = webdriver.Chrome("C:/Users/Rajas/chromedriver_win32/chromedriver.exe")
ser = Service("C:/Users/Rajas/geckodriver_win32/geckodriver.exe")
# driver = webdriver.Firefox(executable_path= "C:/Users/Rajas/geckodriver_win32/geckodriver.exe")
op = webdriver.FirefoxOptions()

options = Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

driver = webdriver.Firefox(service=ser, options=options)
print("Login test cases started")  
driver.get("https://reading-loop-528f8.web.app/login")
driver.maximize_window()  
time.sleep(2)
signups = [{"email": "", "password": "Kk4GLcjLT5mUbdX" , "result": ""},
            {"email": "rajas.bondale", "password": "Kk4GLcjLT5mUbdX" , "result": ""},
            {"email": "12312212", "password": "Kk4GLcjLT5mUbdX" , "result": ""},
            {"email": "rajas.bondale@somaiya.edu", "password": "" , "result": ""},
            {"email": "", "password": "" , "result": ""},
            {"email": "rajas.bondale@somaiya.edu", "password": "Kk4GLcjLT5mUbdX" , "result": ""},
            ]
email = driver.find_element("name", "email")
email.send_keys("email")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
password = driver.find_element("name", "password")
myele = driver.find_element("xpath", "//button[@class='rounded-filled-btn'][contains(., 'Login')]")
for i in signups:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    email.clear()
    password.clear()
    email.send_keys(i["email"])
    password.send_keys(i["password"])
    myele.click()
    time.sleep(2)
    i["result"] = driver.find_element("id", "notistack-snackbar").text
    driver.find_element("css selector", ".SnackbarItem-action").find_element("tag name", "button").click()
    time.sleep(1)
print(signups)
df = pd.DataFrame.from_dict(signups)
df.to_csv("login.csv")
time.sleep(2)
driver.close()  
print("Sample test cases successfully completed")  