from locators import DroppableLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions
from pages.base_page import BasePage

class DroppablePage(BasePage):

    def drop_the_element(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(DroppableLocators.DROPPABLE_ELEMENT))
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(DroppableLocators.TARGET_ELEMENT))
        droppableElement = self.driver.find_element(*DroppableLocators.DROPPABLE_ELEMENT)
        targetElement = self.driver.find_element(*DroppableLocators.TARGET_ELEMENT)
        ActionChains(self.driver).drag_and_drop(droppableElement,targetElement).perform()

    def get_target_element_text(self):
        return self.driver.find_element(*DroppableLocators.TARGET_ELEMENT).text

    def get_target_element_color(self):
        return self.driver.find_element(*DroppableLocators.TARGET_ELEMENT).value_of_css_property('color')