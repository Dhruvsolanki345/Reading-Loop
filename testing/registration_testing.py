from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import pandas as pd
from csv import DictReader

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
with open("registration_input.csv", 'r') as f:
    dict_reader = DictReader(f)
    signups = list(dict_reader)

# signups = [{"name": "",       "email": "rajas@gmail.com", "phone": "9969342104",   "password": "password", "agreeTerms": True, "result": ""},
#             {"name": "Rajas", "email": "rajas@gmail.com", "phone": "9969342104",   "password": "password", "agreeTerms": True, "result": ""},
#             {"name": "",       "email": ""              ,"phone": "",              "password": "",         "agreeTerms": True, "result": ""},
#             {"name": "Rajas", "email": "",                "phone": "9969342104",   "password": "password", "agreeTerms": True, "result": ""},
#             {"name": "Rajas", "email": "rajas",           "phone": "9969342104",   "password": "password", "agreeTerms": True, "result": ""},
#             {"name": "Rajas", "email": "rajas@gmail.com", "phone": "",             "password": "password", "agreeTerms": True, "result": ""},
#             {"name": "Rajas", "email": "rajas@gmail.com", "phone": "abcdefgh",     "password": "password", "agreeTerms": True, "result": ""},
#             {"name": "Rajas", "email": "rajas@gmail.com", "phone": "996934210",    "password": "password", "agreeTerms": True, "result": ""},
#             # {"name": "Rajas", "email": "rajas@gmail.com", "phone": "996934210412", "password": "password", "agreeTerms": True, "result": ""},
#             {"name": "Rajas", "email": "rajas@gmail.com", "phone": "9969342104",   "password": "",         "agreeTerms": True, "result": ""},
#             {"name": "Rajas", "email": "rajas@gmail.com", "phone": "9969342104",   "password": "pass",     "agreeTerms": True, "result": ""},
#             {"name": "Rajas", "email": "rajas@gmail.com", "phone": "9969342104",   "password": "password", "agreeTerms": False, "result": ""},
#             ]
name = driver.find_element("name", "name")
email = driver.find_element("name", "email")
phone = driver.find_element("name", "phone")
password = driver.find_element("name", "password")
agreeTerms = driver.find_element("name", "agreeTerms")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
myele = driver.find_element("xpath", "//button[@class='rounded-filled-btn'][contains(., 'Sign Up')]")
for i in signups:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    name = driver.find_element("name", "name")
    email = driver.find_element("name", "email")
    phone = driver.find_element("name", "phone")
    password = driver.find_element("name", "password")
    agreeTerms = driver.find_element("name", "agreeTerms")
    myele = driver.find_element("xpath", "//button[@class='rounded-filled-btn'][contains(., 'Sign Up')]")
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
df = pd.DataFrame.from_dict(signups)
df.to_csv("registration.csv")
driver.close()  
print("sample test case successfully completed")  
