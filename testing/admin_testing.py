from selenium import webdriver
import time
import os
from pprint import pprint

base = os.getcwd()
driver = webdriver.Chrome()

print("Admin test cases started")
driver.get("https://reading-loop-528f8.web.app/login")
driver.maximize_window()

time.sleep(1)

# login in to access the admin page
crend = {"email": "dhruv@gmail.com", "password": "12345678"}
email = driver.find_element("name", "email")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
password = driver.find_element("name", "password")
login_btn = driver.find_element("xpath", "//button[@class='rounded-filled-btn'][contains(., 'Login')]")
email.send_keys(crend["email"])
password.send_keys(crend["password"])
login_btn.click()

time.sleep(3)

# open admin page
admin_link = driver.find_element("xpath", "/html/body/div/div/div[1]/div[2]/div/ul/li[2]/button")
admin_link.click()

time.sleep(1)

# open upload page
upload_btn = driver.find_element('xpath', '/html/body/div/div/div[3]/div/div/button')
upload_btn.click()

time.sleep(1)

# test cases to test upload form
test_cases = [
    {"title": "", "file_present": False, "author": "", "result": ""}, 
    {"title": "Book 1", "file_present": False, "author": "", "result": ""},
    {"title": "Book 1", "file_present": True, "file_url": base + "\\dummy.pdf", "author": "", "result": ""},
    {"title": "Book 1", "file_present": True, "file_url": base + "\\dummy.jpg", "author": "", "result": ""},
    {"title": "Book 1", "file_present": True, "file_url": base + "\\dummy.pdf", "author": "Dhruv", "result": ""},
    ]

# reference of necessary elements 
title = driver.find_element("name", "title")
file = driver.find_element("xpath", '/html/body/div/div/div[3]/div/div/div[3]/input')
author = driver.find_element("name", "author")
save_btn = driver.find_element("xpath", '/html/body/div/div/div[3]/div/div/button')

# execute test cases
for test_case in test_cases:
    title.clear()
    file.clear()
    author.clear()
    title.send_keys(test_case['title'])
    author.send_keys(test_case['author'])

    if test_case['file_present']:
        file.send_keys(test_case['file_url'])
       
    save_btn.click()
    time.sleep(2)
    test_case["result"] = driver.find_element("id", "notistack-snackbar").text
    driver.find_element("css selector", ".SnackbarItem-action").find_element("tag name", "button").click()
    time.sleep(1)

pprint(test_cases)

time.sleep(2)
driver.close()
print("Admin test cases successfully completed")