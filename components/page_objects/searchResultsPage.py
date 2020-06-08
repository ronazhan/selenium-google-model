from selenium.webdriver.common.by import By
from basePage import BasePage
from selenium.webdriver.common.keys import Keys

class SearchResultsPage(BasePage):
    def __init__(self, basePageObj, keywords):
        BasePage.__init__(self, basePageObj.driver)
        self.navigateToPage("https://www.google.com/")
        searchBar = self.findElement(By.XPATH, "//*[contains(@name,'q')]")
        searchBar.send_keys(keywords + Keys.ENTER)

    locator_dictionary = {
        "Home": (By.XPATH, "//*[contains(@id, 'logo')]"),
        "Results": (By.CLASS_NAME, 'r'),
        "Images": (By.XPATH, "//*[contains(@href,'img')]"),
        "SearchBar": (By.XPATH, "//*[contains(@name,'q')]"),
        "SearchButton": (By.XPATH, "//*[contains(@name,'btnK')]"),
        'NextResultPage': (By.XPATH, "//*[contains(@id,'pnnext')]"),
        'News': (By.LINK_TEXT, "News"),
        'Maps': (By.LINK_TEXT, 'Maps'),
        "SearchResultsTitle": (By.XPATH, "//*[contains(@title, '')]")
    }

    def isSearchPage(self, retryCount=0, timeout=None, restartWebDriver=False, quitWebdriver=False):
        return self.checkElementonPage(
            locatorName=self.getElement('SearchResultsTitle', True),
            locatorMessage='Google Search',
            retryCount=retryCount,
            timeout=timeout,
            restartWebDriver=restartWebDriver,
            quitWebdriver=quitWebdriver
        )

    def clickHome(self):
        self.getElement("Home", False).click()

    def getSearchBar(self):
        self.getElement("SearchBar", False)

    def goToResultPage(self):
        self.getElement("NextResultPage", False).click()

    def getResultsText(self):
        res = self.getElements("Results", False)
        return [r.text for r in res if len(r.text)>0]

    def goToNews(self):
        self.getElement("News", False).click()

    def goToMaps(self):
        self.getElement("Maps", False).click

    def search(self, keywords, exception=None):
        if exception != None:
            raise exception

        searchBar = self.getSearchBar()
        searchBar.send_keys(keywords + Keys.ENTER)