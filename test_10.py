import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Search(unittest.TestCase):

    def setUp(self):
        self.drv = webdriver.Chrome(executable_path='F:\\python\\chromedriver_win32\\chromedriver.exe')
        self.url = 'http://www.google.com'
        self.drv.get(self.url)

    def test_search(self):
        assert 'Google' in self.drv.title
        self.elm = self.drv.find_element_by_name('q')
        self.elm.send_keys('selenide')
        self.elm.send_keys(Keys.RETURN)

        link01 = self.drv.find_element_by_xpath('//div/cite')
        assert "selenide.org" in link01.text.lower()

        self.drv.find_element_by_xpath('//*[@class="hdtb-mitem"][2]/a[@href]').click()

        link02 = self.drv.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]')
        assert "selenide.org" in link02.text.lower()

        self.drv.find_element_by_xpath('//*[@jsname ="ONH4Gc"]').click()

        link04 = self.drv.find_element_by_xpath('//div/cite')
        assert "selenide.org" in link04.text.lower()

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()
