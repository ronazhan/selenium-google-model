from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    driver = None
    DEFAULT_TIMEOUT = 10
    __timeout = DEFAULT_TIMEOUT

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome("../drivers/chromedriver")

    def getCurrentURL(self):
        return self.driver.current_url

    def deleteSession(self):
        self.quitWebdriver()

    def navigateToPage(self, url):
        self.driver.get(url)

    def refreshCurrentPage(self):
        self.driver.get(self.driver.current_url)

    def getElement(self, locatorName, returnLocatorName=False):
        return locatorName if returnLocatorName else self.findElement(*self.locator_dictionary[locatorName])

    def getElements(self, locatorName, returnLocatorName=False):
        """
        Returns all the occurences of a matching pattern available on the web page
        """
        return locatorName if returnLocatorName else self.findElements(*self.locator_dictionary[locatorName])

    def findElements(self, *loc):
        try:
            return self.driver.find_elements(*loc)
        except Exception as e:
            return loc

    def findElement(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except (NoSuchElementException):
            return loc

    def quitWebdriver(self):
        self.driver.close()

    def restartWebdriver(self):
        self.quitWebdriver()
        self.driver = self.instantiateWebdriver()
        self.setTimeout(self.DEFAULT_TIMEOUT)

    def getTimeout(self):
        if not self.__timeout:
            self.__timeout = self.DEFAULT_TIMEOUT
        return self.__timeout

    def setTimeout(self, timeout=None):
        if not timeout:
            self.__timeout = self.DEFAULT_TIMEOUT
        else:
            self.__timeout = timeout

    def __getattr__(self, locatorName):
        try:
            if locatorName in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.driver, self.getTimeout()).until(
                        EC.presence_of_element_located(self.locator_dictionary[locatorName])
                    )
                except (TimeoutException, StaleElementReferenceException):
                    return None

                try:
                    element = WebDriverWait(self.driver, self.getTimeout()).until(
                        EC.visibility_of_element_located(self.locator_dictionary[locatorName])
                    )
                except (TimeoutException, StaleElementReferenceException):
                    return None
                return self.findElement(*self.locator_dictionary[locatorName])
        except AttributeError:
            super(BasePage, self).__getattribute__("methodMissing")(locatorName)

    def waitForElement(self, locatorName, timeout=None):
        self.setTimeout(timeout)
        try:
            WebDriverWait(self.driver, self.getTimeout()).until(
                EC.visibility_of_element_located(self.locator_dictionary[locatorName])
            )
        except (TimeoutException, StaleElementReferenceException):
            return False
        return True

    def waitForElementInvisibility(self, locatorName, timeout=None):
        self.setTimeout(timeout)
        try:
            WebDriverWait(self.driver, self.getTimeout()).until(
                EC.invisibility_of_element_located(self.locator_dictionary[locatorName])
            )
        except (TimeoutException, StaleElementReferenceException):
            return False
        return True

    def methodMissing(self, locatorName):
        print "No %s here!" % locatorName

    def instantiateWebdriver(self):
        self.driver = webdriver.Chrome("../drivers/chromedriver")

    def checkElementonPage(
            self, locatorName, locatorMessage, retryCount=0, timeout=None, restartWebDriver=False, quitWebdriver=False
    ):
        self.setTimeout(timeout)
        if self.__getattr__(locatorName):
            return True
        else:
            if retryCount > 0:
                if restartWebDriver:
                    self.restartWebdriver()
                return self.checkElementonPage(
                    locatorName, locatorMessage, retryCount - 1, timeout, restartWebDriver, quitWebdriver
                )
            else:
                if quitWebdriver:
                    self.quitWebdriver()
                    exit(1)
            return False

    def validateSortingOrder(self, inputList, orderType='ascending'):
        """
        A general function that accepts a list as input parameter and
        validates if the list is sorted properly as per orderType
        """
        sortedList = []
        if orderType == 'ascending':
            if isinstance(inputList[0], int):
                sortedList = sorted(inputList)
            else:
                # The current sorting order implemented on the cluster table
                # is case insensitive, hence support for the same
                sortedList = sorted(inputList, key=lambda s: s.lower())
        elif orderType == 'descending':
            if isinstance(inputList[0], int):
                sortedList = sorted(inputList, reverse=True)
            else:
                sortedList = sorted(inputList, reverse=True, key=lambda s: s.lower())
        # Let's validate the input list and sorted list now
        if inputList == sortedList:
            return True
        else:
            return False
