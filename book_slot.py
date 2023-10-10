"""
Booking Football Slot

Script for booking an astro for football using Selenium
"""

__date__ = "2023-10-10"
__author__ = "JamesMcGonigle"

# %% --------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from secret_keys import email, password, driver_path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

import datetime
import time


# %% --------------------------------------------------------------------------
# Chose constants
# -----------------------------------------------------------------------------
current_date = datetime.date.today()

# You can only book for 6 days in the future
six_days_from_now = current_date + datetime.timedelta(days=6)


# %% --------------------------------------------------------------------------
#  Set up Web Driver
# -----------------------------------------------------------------------------
driver = webdriver.Chrome(driver_path)

url = fr'https://bookings.better.org.uk/location/finsbury-leisure-centre/threeg-5-a-side/{current_date}/by-time'
# url = fr'https://bookings.better.org.uk/location/finsbury-leisure-centre/threeg-5-a-side/{six_days_from_now}/by-time'

driver.get(url)


# %% --------------------------------------------------------------------------
# Logging In
# -----------------------------------------------------------------------------
# click on log in 
xpath_login = r'/html/body/div[1]/div[1]/div/div/ul/li[3]/button/span'
driver.find_element("xpath", xpath_login).click() 

# email address 
xpath_email = r'/html/body/div[3]/div[3]/form/div[1]/div/input'
driver.find_element("xpath", xpath_email).click() 
driver.find_element("xpath", xpath_email).send_keys(f'{email}')

# password
xpath_email = r'/html/body/div[3]/div[3]/form/div[2]/div/div/input'
driver.find_element("xpath", xpath_email).click() 
driver.find_element("xpath", xpath_email).send_keys(f'{password}', Keys.ENTER)


# %% --------------------------------------------------------------------------
# Finding 20:30 
# -----------------------------------------------------------------------------
target = '20:30 - 21:15'
a = 1 

while True:

    try:
        trying_elements_path = fr'/html/body/div[1]/div[3]/div/div[1]/div/div[5]/div[{a}]/div/div/div[1]/div[1]'
        element = driver.find_element(By.XPATH, trying_elements_path)
        eightthirty = element.text
        
        if eightthirty == target:
            break

    except NoSuchElementException:
        pass

    a += 1

    if a > 15:
        break


# %% --------------------------------------------------------------------------
# Clicking Book
# -----------------------------------------------------------------------------
xpath_book_b = fr'/html/body/div[1]/div[3]/div/div[1]/div/div[5]/div[{a}]/div/div/div[5]/div/div/span/div/a/button/span'
driver.find_element("xpath", xpath_book_b).click() 
