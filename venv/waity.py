from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def wait_time(driver,locator,element):
    return WebDriverWait(driver,15).until(EC.element_to_be_clickable((locator , element)))
    


