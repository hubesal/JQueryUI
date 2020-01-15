from locators import ResizableLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions
from pages.base_page import BasePage

class ResizablePage(BasePage):

    def wait_for_resizables(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(ResizableLocators.RESIZABLE_ELEMENT))
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(ResizableLocators.RESIZE_BOTH_DIRS))

    def get_resizable_element(self):
        return self.driver.find_element(*ResizableLocators.RESIZABLE_ELEMENT)

    def get_resize_anchor_element(self):
        return self.driver.find_element(*ResizableLocators.RESIZE_BOTH_DIRS)

    def resizing_element(self, element, x, y):
        ActionChains(self.driver).click_and_hold(element).move_by_offset(x, y).release().perform()


