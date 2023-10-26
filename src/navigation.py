from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class PageNavigation:
    def __init__(self, webBroswer: str) -> None:
        match str.upper(webBroswer):
            case "CHROME":
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                self.driver = webdriver.Chrome(options)
                self.driver.implicitly_wait(10)
            case "IE":
                options = webdriver.IeOptions()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                self.driver = webdriver.Ie(options)
                self.driver.implicitly_wait(10)
            case "FIREFOX":
                options = webdriver.FirefoxOptions()
                options.binary_location =self._getFirefoxBinary()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                self.driver = webdriver.Firefox(options)
                self.driver.implicitly_wait(10)

    def _getFirefoxBinary(self) -> str:
        firefoxBinary = os.getenv("FIREFOX_BINARY")
        if(firefoxBinary ==  None):
            raise Exception("env var FIREFOX_BINARY must be set")
        else:
            return firefoxBinary

    def navigateToUrl(self, url: str):
        self.driver.get(url)

    def getElementByXPath(self, xPath:str) -> WebElement:
        return self.driver.find_element(By.XPATH,xPath)
    
    def isTextInPage(self, xPath: str,text:str) -> bool:
        try:
            WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.XPATH, xPath),text))
            return True
        except Exception as e:
            print("Failed to get element {exception}".format(exception = e))
            return False
    
    def closeDriver (self):
        self.driver.close()
    

