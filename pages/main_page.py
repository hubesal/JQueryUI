from locators import MainPageLocators
from pages.base_page import BasePage

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    def click_draggable_link(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(MainPageLocators.DRAGGABLE_LINK))
        self.driver.find_element(*MainPageLocators.DRAGGABLE_LINK).click()

    def click_droppable_link(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(MainPageLocators.DROPPABLE_LINK))
        self.driver.find_element(*MainPageLocators.DROPPABLE_LINK).click()

    def click_resizable_link(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(MainPageLocators.RESIZABLE_LINK))
        self.driver.find_element(*MainPageLocators.RESIZABLE_LINK).click()