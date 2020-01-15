from locators import BasePageLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_frame(self):
        WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it(BasePageLocators.FRAME))

