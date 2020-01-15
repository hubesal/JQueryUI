from locators import DraggableLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions
from pages.base_page import BasePage


class DraggablePage(BasePage):

    def drag_and_drop(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(DraggableLocators.SQUARE))
        self.square = self.driver.find_element(*DraggableLocators.SQUARE)

    def drag_on_the_screen(self, area, x, y):
        ActionChains(self.driver).drag_and_drop_by_offset(area, x, y).perform()
