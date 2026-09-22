from helpers.locators import ALL_TIME_ORDERS_FINISHED, IN_PROGRESS, ORDERS_LIST, TODAY_ORDERS_FINISHED
from pages.base_page import BasePage


class FeedPage(BasePage):

    def orders_list_is_visible(self):
        self.find_element(ORDERS_LIST)
        return True

    def get_all_time_orders(self):
        return int(self.get_text(ALL_TIME_ORDERS_FINISHED))

    def get_today_orders(self):
        return int(self.get_text(TODAY_ORDERS_FINISHED))

    def in_progress_has_number(self, number):
        text = self.get_text(IN_PROGRESS)
        return str(number) in text