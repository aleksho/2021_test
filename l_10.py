from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drv = webdriver.Chrome(executable_path='F:\\python\\chromedriver_win32\\chromedriver.exe')
url = 'http://www.google.com'
drv.get(url)
assert 'Google' in drv.title
elm = drv.find_element_by_name('q')
elm.send_keys('selenide')
elm.send_keys(Keys.RETURN)

link01 = drv.find_element_by_xpath('//div/cite')
assert "selenide.org" in link01.text.lower()

drv.find_element_by_xpath('//*[@class="hdtb-mitem"][2]/a[@href]').click()

link02 = drv.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]')
assert "selenide.org" in link02.text.lower()

drv.find_element_by_xpath('//*[@jsname ="ONH4Gc"]').click()

link04 = drv.find_element_by_xpath('//div/cite')
assert "selenide.org" in link04.text.lower()

print('Done')
