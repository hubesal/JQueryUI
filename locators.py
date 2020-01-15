from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePageLocators:

    FRAME = (By.TAG_NAME, 'iframe')

class MainPageLocators:

    DRAGGABLE_LINK = (By.LINK_TEXT, "Draggable")
    DROPPABLE_LINK = (By.LINK_TEXT, "Droppable")
    RESIZABLE_LINK = (By.LINK_TEXT, 'Resizable')

class DraggableLocators:

    SQUARE = (By.XPATH, "//*[@id='draggable']")

class DroppableLocators:

    DROPPABLE_ELEMENT = (By.ID, 'draggable')
    TARGET_ELEMENT = (By.ID, 'droppable')

class ResizableLocators:

    RESIZE_BOTH_DIRS = (By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
    RESIZE_X_AXIS = (By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-e']")
    RESIZE_Y_AXIS = (By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-s']")
    RESIZABLE_ELEMENT = (By.ID, "resizable")