import time
from page_objects.basePage import BasePage
from page_objects.homePage import HomePage
from page_objects.searchResultsPage import SearchResultsPage
from page_objects.googleLoginPage import GoogleLoginPage
from selenium.common.exceptions import NoSuchElementException
import pytest

def test_open_home_page():
    basePage = BasePage()
    homePage = HomePage(basePage)
    assert homePage.isHomePage()

    time.sleep(5)
    homePage.deleteSession()

@pytest.mark.parametrize(
    "exception",
    [(NoSuchElementException), (None)]
)
def test_search_home_page(exception):
    basePage = BasePage()
    homePage = HomePage(basePage)
    assert homePage.isHomePage()

    # Seach for Hortonworks
    # May need second attempt if page has not finished loading or simulating exception
    try:
        homePage.search("Hortonworks", exception)
    except NoSuchElementException:
        time.sleep(5)
        homePage.search("Hortonworks", None)

    time.sleep(5)
    homePage.deleteSession()

@pytest.mark.parametrize(
    "exception",
    [(NoSuchElementException), (None)]
)
def test_open_about(exception):
    basePage = BasePage()
    homePage = HomePage(basePage)
    assert homePage.isHomePage()

    try:
        homePage.goToAboutPage(exception)
    except NoSuchElementException:
        time.sleep(5)
        homePage.goToAboutPage()

    time.sleep(5)
    homePage.deleteSession()

# Tries logging in
# Should fail because Google does not allow logins from automated browser
def test_login():
    basePage = BasePage()
    googleLoginPage = GoogleLoginPage(basePage)

    try:
        googleLoginPage.login("rozhang@gmail.com", "gibberish")
    except Exception as e:
        assert type(e) == AttributeError
        time.sleep(5)
        basePage.deleteSession()



def test_search():
    basePage = BasePage()
    searchResultsPage = SearchResultsPage(basePage, "Cloudera")
    assert searchResultsPage.isSearchPage()

    searchResultsPage.goToMaps()
    time.sleep(5)
    basePage.deleteSession()

def test_results_list():
    basePage = BasePage()
    searchResultsPage = SearchResultsPage(basePage, "Cloudera")
    assert searchResultsPage.isSearchPage()

    res = searchResultsPage.getResultsText()
    assert str(res[0]).find("www.cloudera.com") != -1
    time.sleep(5)
    basePage.deleteSession()