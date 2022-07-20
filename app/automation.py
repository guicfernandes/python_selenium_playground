from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.by import By

# Instantiating a chrome driver
chrome_browser = webdriver.Chrome('./chromedriver.exe')

# maximize window
chrome_browser.maximize_window()
# request a webpage
chrome_browser.get('https://www.seleniumeasy.com/')

# using assert to identify things
# assert 'Selenium Easy' in chrome_browser.title
assert 'Selenium Easy' in chrome_browser.page_source

# button = chrome_browser.find_element(By.CLASS_NAME, 'btn-grey')
# print(button.get_attribute('innerHTML'))

# find element by name on page, clearing it and writing on it
user_search = chrome_browser.find_element(By.NAME, 'search_block_form')
user_search.clear()
user_search.send_keys('Run tests in parallel with pytest')

# find elemtent button by class name and clicking it
button_search = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
button_search.click()

# asserting the instruction was done
output_search = chrome_browser.find_element(By.CLASS_NAME, 'title')
assert 'Run tests in parallel with pytest' in output_search.text

# closing chrome window
# chrome_browser.close()

# quiting webdriver
chrome_browser.quit()
