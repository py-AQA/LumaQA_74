from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from base.seleniumbase import BasePage
from locators.wish_list_locators import WishListLocators


class TestWishList:

    def test_visibility_items_left_corner(self, driver, open_main_page, sign_in, add_items_to_wish_list):
        wait(driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located(WishListLocators.WISH_LIST_SIDEBAR_ITEMS))
        wish_list_elements = driver.find_elements(*WishListLocators.WISH_LIST_SIDEBAR_ITEMS)
        wish_list = [element.text for element in wish_list_elements]
        assert len(wish_list) >= 1, "Items not found"
