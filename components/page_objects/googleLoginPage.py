from basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleLoginPage(BasePage):
    def __init__(self, basePageObj):
        BasePage.__init__(self, driver=basePageObj.driver)
        self.navigateToPage("https://www.google.com/")
        self.findElement(By.XPATH, "//*[contains(@href, 'accounts.google')]").click()

    locator_dictionary = {
        "username": (By.NAME, "identifier"),
        "password": (By.NAME, "password"),
        "identifierNext": (By.ID, "identifierNext"),
        "passwordNext": (By.ID, "passwordNext"),
        "LoginPageTitle": (By.XPATH, "//*[contains(@title, 'Sign in')]")
    }

    def isLoginPage(self, retryCount=0, timeout=None, restartWebDriver=False, quitWebdriver=False):
        return self.checkElementonPage(
            locatorName=self.getElement('LoginPageTitle', True),
            locatorMessage='Sign in - Google Accounts',
            retryCount=retryCount,
            timeout=timeout,
            restartWebDriver=restartWebDriver,
            quitWebdriver=quitWebdriver
        )

    def getEmailTextBox(self, returnLocatorName=False):
        return self.getElement("username", returnLocatorName)

    def getPasswordTextBox(self, returnLocatorName=False):
        return self.getElement("password", returnLocatorName)

    def getIdentifierNext(self, returnLocatorName=False):
        return self.getElement("identifierNext", returnLocatorName)

    def getPasswordNext(self, returnLocatorName=False):
        return self.getElement("passwordNext", returnLocatorName)

    def login(self, user, pswd):
        emailElem = self.getElement("username", False)
        emailElem.send_keys(user + Keys.ENTER)

        passElem = self.waitForElement("password")
        passElem.send_keys(pswd + Keys.ENTER)
