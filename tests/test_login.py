from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time

chrome_path="driver/chromedriver.exe"
base_url = "https://www.saucedemo.com/"
serv = Service(chrome_path)
driver = webdriver.Chrome(service=serv)


class Login(unittest.TestCase):

    def open_browser(self):
        driver.get(base_url)
        driver.maximize_window()
    
    def input_username(self):
        username_field = driver.find_element(By.ID, 'user-name')
        username_field.send_keys("standard_user")
        
    def input_password(self, password):
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys(password)
        
    def click_login_button(self):
        login_btn = driver.find_element(By.ID, 'login-button')
        login_btn.click()
        
    def test_valid_login(self):
        login = Login()
        login.open_browser()
        login.input_username()
        login.input_password("secret_sauce")
        login.click_login_button()

        product_title = driver.find_element(By.XPATH, '//span[text()= "Products"]')
        assert product_title.is_displayed() == True
    
    def test_failed_login(self):
        login = Login()
        login.open_browser()
        login.input_username()
        login.input_password("salah_password")
        login.click_login_button()
        
        error_message = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        actual = error_message.text
        assert actual == "Epic sadface: Username and password do not match any user in this service"