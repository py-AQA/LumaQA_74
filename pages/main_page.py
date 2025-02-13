from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'

    def check_visibility_the_title(self):
        return self.is_visible(BasePageLocators.LOGO_TITLE)

    def check_visibility_of_erin_recommends_widget(self):
        return self.is_visible(BasePageLocators.ERIN_SECTION)

    def check_clickability_of_erin_recommends_widget(self):
        return self.is_clickable(BasePageLocators.ERIN_SECTION)

    def scroll_down_to_shop_erin_recom(self):
        self.scroll_to_element(BasePageLocators.SHOP_ERIN_RECOMMENDS)

    def men_btn_catalog(self):
        return self.is_clickable(BasePageLocators.LINK_MEN)

    def select_tops_from_mens_dropdown_menu(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_MEN)
        self.is_clickable(BasePageLocators.LINK_MEN_TOPS)

    def select_bottoms_from_mens_dropdown_menu(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_MEN)
        self.is_clickable(BasePageLocators.LINK_MEN_BOTTOMS)

    def visibility_of_men_tops_secondary_dropdown_menu(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_MEN_TOPS)
        return self.is_visible(BasePageLocators.LINK_MEN_TOPS_JACKETS)

    def visibility_of_men_bottoms_secondary_dropdown_menu(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_MEN_BOTTOMS)
        return self.is_visible(BasePageLocators.LINK_MEN_BOTTOMS_PANTS)

    def scroll_down_to_shop_performance(self):
        self.scroll_to_element(BasePageLocators.SHOP_PERFORMANCE)

    def check_images_boxes_on_page(self):
        results = []
        for block_selector in BasePageLocators.LIST_IMAGES:
            block_present = self.is_visible(block_selector)
            results.append(block_present)
        return results

    def scroll_down_to_shop_eco_friendly(self):
        self.scroll_to_element(BasePageLocators.SHOP_ECO_FRIENDLY)

    def check_that_all_elements_are_visible(self, link_1):
        element = self.is_visible(link_1)
        assert element.is_displayed() and element.is_enabled(), 'Элемент не виден  или не доступен для нажатия'

    def compare_words(self, TYPED_WORD):
        elem = self.is_clickable(BasePageLocators.HEADER_SEARCHBAR)
        elem.click()
        elem.clear()
        elem.send_keys(TYPED_WORD)
        search_loc = self.is_visible(BasePageLocators.SEARCHING_RESULT)
        assert TYPED_WORD in search_loc.text, 'фрагмент слова, набранный в поле поиска, не встречается в подсказанных вариантах'

