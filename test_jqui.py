from selenium import webdriver
import selenium.common.exceptions

import unittest
import time

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.draggable_page import DraggablePage
from pages.droppable_page import DroppablePage
from pages.resizable_page import ResizablePage

class TestJQueryUI(unittest.TestCase):
    
    def setUp(self):

        self.driver = webdriver.Firefox(executable_path=r'C:\Users\pansa\Documents\Webdrivers\geckodriver.exe')
        self.driver.delete_all_cookies()
        self.driver.get('https://jqueryui.com')


    def test_draggable(self):

        mainpage = MainPage(self.driver)
        mainpage.click_draggable_link()
        #switch to frame
        mainpage.switch_to_frame()
        #drag and drop draggable square
        draggablepage = DraggablePage(self.driver)
        draggablepage.drag_and_drop()

        coords = [[60, 45], [-200, -200], [400, 500]]
        correctPositionCounter = 0

        for i in range(len(coords)):
           try:
                draggablepage.drag_on_the_screen(draggablepage.square, coords[i][0], coords[i][1])
                correctPositionCounter += 1
           except selenium.common.exceptions.MoveTargetOutOfBoundsException:
                pass
           if i > 0:
               self.assertRaises(selenium.common.exceptions.MoveTargetOutOfBoundsException)
               correctPositionCounter += 1

        self.assertEqual(correctPositionCounter, len(coords))


    def test_droppable(self):

        #click the link
        mainpage = MainPage(self.driver)
        mainpage.click_droppable_link()

        #switch to frame
        droppablepage = DroppablePage(self.driver)
        droppablepage.switch_to_frame()

        #perform an action
        droppablepage.drop_the_element()

        #assert
        self.assertEqual(str(droppablepage.get_target_element_text()), "Dropped!")
        self.assertTrue(droppablepage.get_target_element_color() == 'rgb(119, 118, 32)')

    def test_resizable(self):
        #click the link
        mainpage = MainPage(self.driver)
        mainpage.click_resizable_link()

        #switch to frame
        resizablepage = ResizablePage(self.driver)
        resizablepage.switch_to_frame()

        resizablepage.wait_for_resizables()
        #perform action
        resizeValues = [[120, 120], [60, 0], [0, 60]]
        correctSize = 0

        for i in range(len(resizeValues)):

            # get element size - before resizing
            sizeXbefore = resizablepage.get_resizable_element().value_of_css_property('width')[0:3]
            sizeYbefore = resizablepage.get_resizable_element().value_of_css_property('height')[0:3]

            try:
                resizablepage.resizing_element(resizablepage.get_resize_anchor_element(), resizeValues[i][0], resizeValues[i][1])
                sizeXAfter = resizablepage.get_resizable_element().value_of_css_property('width')[0:3]
                sizeYAfter = resizablepage.get_resizable_element().value_of_css_property('height')[0:3]
                if (sizeXAfter > sizeXbefore and sizeYAfter > sizeYbefore and i == 0) or (sizeXAfter > sizeXbefore and sizeYAfter == sizeYbefore and i == 1) or (sizeXAfter == sizeXbefore and sizeYAfter > sizeYbefore and i == 2):
                    correctSize += 1
            except selenium.common.exceptions.MoveTargetOutOfBoundsException:
                pass

        self.assertEqual(correctSize, len(resizeValues))


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)

