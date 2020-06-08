from selenium.webdriver.common.by import By
from basePage import BasePage
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    def __init__(self, basePageObj):
        BasePage.__init__(self, basePageObj.driver)
        self.navigateToPage("https://www.google.com/")

    locator_dictionary = {
        "About": (By.XPATH, "//*[contains(@href, 'about.google')]"),
        "Store": (By.XPATH, "//*[contains(@href,'store.google')]"),
        "Images": (By.XPATH, "//*[contains(@href,'img')]"),
        "Description": (By.PARTIAL_LINK_TEXT, "howsearchworks"),
        "SearchBar": (By.XPATH, "//*[contains(@name,'q')]"),
        "SearchButton": (By.XPATH, "//*[contains(@name,'btnK')]"),
        "HomePageTitle": (By.XPATH, "//*[contains(@title, 'Google')]")
    }
    def isHomePage(self, retryCount=0, timeout=None, restartWebDriver=False, quitWebdriver=False):
        return self.checkElementonPage(
            locatorName=self.getElement('HomePageTitle', True),
            locatorMessage='Google',
            retryCount=retryCount,
            timeout=timeout,
            restartWebDriver=restartWebDriver,
            quitWebdriver=quitWebdriver
        )

    def search(self, keywords, exception):
        if exception:
            raise exception

        searchBar = self.getSearchBar(False)
        searchBar.send_keys(keywords + Keys.ENTER)

    def getSearchBar(self, returnLocatorName=False):
        return self.getElement("SearchBar", returnLocatorName)

    def clickSearchButton(self, returnLocatorName=False):
        self.getElement("SearchButton", returnLocatorName).click()

    def goToImages(self,returnLocatorName=False):
        self.getElement("Images", returnLocatorName).click()

    def goToAboutPage(self, exception=None, returnLocatorName=False):
        if exception:
            raise exception
        self.getElement('About', returnLocatorName).click()

    def goToStore(self, returnLocatorName=False):
        self.getElement('Store', returnLocatorName).click()

    def goToDescription(self, returnLocatorName=False):
        self.getElement('Description', returnLocatorName).click()

