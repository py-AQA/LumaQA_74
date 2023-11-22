from base.seleniumbase import BasePage
from selenium.webdriver.common.by import By
from data.privacy_and_cookie_policy_page_urls import PRIVACY_AND_COOKIE_POLICY_PAGE
from data.privacy_and_cookie_policy_page_fonts import PrivacyCookiePolicyFonts
from locators.privacy_and_cookie_policy_page_locators import PrivacyCookiePolicyPageLocators
import language_tool_python

def test_text_block_font_family_titled_cour_choices_regarding_use_of_the_information_we_collect(driver):
    """TC_012.007.001 | Footer > "Privacy and Cookie Policy" > Content >
     The Font family of the text block titled "Your Choices Regarding Use Of The Information We Collect"""
    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    element = driver.find_element(By.XPATH, PrivacyCookiePolicyPageLocators.BLOCK_CONTENT_LOCATOR)
    font_family = element.value_of_css_property('font-family')
    assert font_family == PrivacyCookiePolicyFonts.TEXT_FONT_FAMILY

def test_text_block_header_font_size_titled_cour_choices_regarding_use_of_the_information_we_collect(driver):
    """TC_012.007.002 | Footer > "Privacy and Cookie Policy" > Content >
     The Font-size of the title ‘Your Choices Regarding Use Of The Information We Collect’"""
    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    element = driver.find_element(By.XPATH, PrivacyCookiePolicyPageLocators.BLOCK_CONTENT_HEADER_LOCATOR)
    font_size = element.value_of_css_property('font-size')
    assert font_size == PrivacyCookiePolicyFonts.HEADER_TEXT_FONT_SIZE

def test_text_block_font_size_titled_cour_choices_regarding_use_of_the_information_we_collect(driver):
    """TC_012.007.003 | Footer > "Privacy and Cookie Policy" > Content >
     The Font-size of the text of the block titled 'Your Choices Regarding Use Of The Information We Collect'"""
    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    element = driver.find_element(By.XPATH, PrivacyCookiePolicyPageLocators.BLOCK_CONTENT_LOCATOR)
    font_size = element.value_of_css_property('font-size')
    assert font_size == PrivacyCookiePolicyFonts.TEXT_FONT_SIZE

def test_text_block_for_typos_titled_your_choices_regarding_use_of_the_information_we_collect(driver):
    """TC_012.007.004 | Footer > "Privacy and Cookie Policy" > Content > Verify the text block and title for typos
    titled ‘Your Choices Regarding Use Of The Information We Collect’"""
    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    text_header = driver.find_element(By.XPATH, PrivacyCookiePolicyPageLocators.BLOCK_CONTENT_HEADER_LOCATOR).text
    text_block = driver.find_element(By.XPATH, PrivacyCookiePolicyPageLocators.BLOCK_CONTENT_LOCATOR).text
    tool = language_tool_python.LanguageTool('en-US')
    matches_header = tool.check(text_header)
    assert len(matches_header) == 0, f"Grammar mistakes have been found in the header: {matches_header}"
    matches_block = tool.check(text_block)
    assert len(matches_block) == 0, f"Grammar mistakes have been found in the text block: {matches_block}"

