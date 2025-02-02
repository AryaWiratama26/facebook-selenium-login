from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

time.sleep(3)

# Masukin email dan pass
input_email = input("Masukkan email: ")
input_pass = input("Masukkan password: ")

# Cari input email dan send_keys input email
cari_email_input = driver.find_element(By.ID, "email")
cari_email_input.send_keys(input_email)

# Cari input password dan send_keys input password
cari_pass_input = driver.find_element(By.ID, "pass")
cari_pass_input.send_keys(input_pass)

# Cari button login dan klik buat login
login = driver.find_element(By.NAME, "login")
login.click()

time.sleep(5)

input("")
driver.quit()
