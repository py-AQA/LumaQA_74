import pytest
import random

from faker import Faker
from base.seleniumbase import BasePage
from data.men_page_url import MEN_TOPS_JACKETS_PAGE
from locators.login import LOGIN_PAGE, LOGAUT_PAGE
from pages.account.create_account import CreateAccountPage
from pages.item_page import ItemPage, ItemDetailsPage
from pages.login.login_page import LoginPage
from pages.my_account.address_book_page import AddressBookPage
from locators.men_page_locators import MenCategoryPageLocators as MenCPL
from pages.men_page import MenJacketsPage


@pytest.fixture
def first_name():
    return Faker().first_name()


@pytest.fixture
def last_name():
    return Faker().last_name()


@pytest.fixture
def email():
    return Faker().email()


@pytest.fixture
def password():
    return Faker().password()


@pytest.fixture
def state():
    return Faker().state()


@pytest.fixture
def postcode():
    return Faker().postcode()


@pytest.fixture
def phone_number():
    return Faker().phone_number()


@pytest.fixture
def street_address():
    return Faker().street_address()


@pytest.fixture
def city():
    return Faker().city()


@pytest.fixture
def create_account(driver):
    CreateAccountPage(driver)


@pytest.fixture
def add_3_item_to_cart(driver):
    page = ItemPage(driver, url=ItemPage.URL_DRIVEN_BACKPACK)
    page.open()
    page.add_driven_backpack_from_item_card_to_cart(3)


@pytest.fixture
def add_first_address_in_account(driver, state, first_name, last_name, phone_number, street_address, city, postcode):
    page = AddressBookPage(driver, url=AddressBookPage.URL_USER_HAS_NO_ADDRESS)
    page.open()
    page.add_new_address(state, first_name, last_name, phone_number, street_address, city, postcode)


@pytest.fixture
def authorization(driver):
    page = LoginPage(driver, LOGIN_PAGE)
    page.open()
    page.sign_in()



@pytest.fixture
def any_page_precondition(driver, any_url):
    base_page = BasePage(driver=driver, url=any_url)
    base_page.open()
    return base_page


@pytest.fixture()
def add_items_to_wish_list(driver):
    lst = ['https://magento.softwaretestingboard.com/breathe-easy-tank.html',
           'https://magento.softwaretestingboard.com/push-it-messenger-bag.html',
           'https://magento.softwaretestingboard.com/ina-compression-short.html',
           'https://magento.softwaretestingboard.com/clamber-watch.html',
           'https://magento.softwaretestingboard.com/tiffany-fitness-tee.html',
           'https://magento.softwaretestingboard.com/ida-workout-parachute-pant.html']
    for href in lst:
        page = ItemDetailsPage(driver, url=href)
        page.add_to_wish_list().click()
        assert page.message.endswith('has been added to your Wish List. Click here to continue shopping.')


@pytest.fixture()
def men_jacket_page(driver):
    page = MenJacketsPage(driver, MEN_TOPS_JACKETS_PAGE)
    page.open()
    return page


@pytest.fixture()
def random_item(driver):
    num_jackets = 11
    jacket_items = [MenCPL.create_item_list(i) for i in range(1, num_jackets + 1)]
    random_jacket = random.choice(jacket_items)
    return random_jacket
