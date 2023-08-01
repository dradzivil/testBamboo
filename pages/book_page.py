import random as r

from pages.base_page import BasePage
from locators.book_page_locators import BookPageLocators as bLocators
from selenium.webdriver.support.select import Select

class BookPage(BasePage):

    def create_booking(self, date='31/07/2024', time='14:00', count=r.randint(1, 4),
                             duration='01:00', hall=0, scheme=0, table=r.randint(0, 3),
                             name='test', phone='7 (912) 345-67-89', comments='Нет комментариев'):
        self.element_is_visible(bLocators.CREATE_BOOK).click()
        self.element_is_visible(bLocators.DATE_OF_BOOK).send_keys(date)
        self.element_is_visible(bLocators.TIME_OF_BOOK).send_keys(time)
        self.element_is_visible(bLocators.COUNT_OF_GUESTS).value = count
        self.element_is_visible(bLocators.DURATION).send_keys(duration)
        Select(self.element_is_visible(bLocators.HALL)).select_by_value(str(hall))
        Select(self.element_is_visible(bLocators.SCHEME)).select_by_value(str(scheme))
        Select(self.element_is_visible(bLocators.TABLE)).select_by_value(str(table))
        self.element_is_visible(bLocators.NAME_GUEST).send_keys(name)
        self.element_is_visible(bLocators.PHONE).send_keys(phone)
        self.element_is_visible(bLocators.COMMENTS).send_keys(comments)
        self.element_is_visible(bLocators.BUTTON_SAVE).click()
