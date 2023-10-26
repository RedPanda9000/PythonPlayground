import unittest
import time
from selenium.webdriver.common.keys import Keys
from navigation import PageNavigation

class TestNavigation(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.browsers = [ "firefox","chrome"]
        super().__init__(methodName)

    def test_navifation_should_be_able_to_enter_text(self):
        expectedXpath = "/html/body/div[5]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/span/a/h3"
        expectedString = "Join us at PyCon"
        for browserStr in self.browsers:
            print("executing test in browser {browser}".format(browser= browserStr))
            unit = PageNavigation(browserStr)
            try:
                unit.navigateToUrl("https://www.google.com")
                self._handleCookies(unit)
                googleInput = unit.getElementByXPath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
                googleInput.clear()
                googleInput.send_keys("pycon")
                time.sleep(2)
                
                googleInput.send_keys(Keys.ENTER)
                self.assertTrue(unit.isTextInPage(expectedXpath,expectedString),"The message should be in the page, browser {browser}".format(browser = browserStr))
            except Exception as e:
                print("error executing the test in browser {browser}".format(browser=browserStr))
                unit.driver.save_screenshot("./test_output/{browser}_result.png".format(browser = browserStr))
            finally:
                unit.closeDriver()
    
    def _handleCookies(self,unit : PageNavigation):
        try:
            rejectGoogleCoockiesButton = unit.getElementByXPath("/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[1]/div")
            rejectGoogleCoockiesButton.click()
        except:
            print("There are no cookies to handle")


if __name__=='__main__':
    unittest.main()
