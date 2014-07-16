# imports
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

# create a new instance of the browser 
driver = webdriver.Firefox()

# URL we are going to test 
driver.get("http://www.giantbomb.com")

#assert that bomb is in the title 
assert "Giant Bomb" in driver.title 

# find login button element on the page
elem = driver.find_element_by_link_text('Log in')

# click the login link
elem.click()

# assert that you are on the correct page 
assert "Login" in driver.title

# find the username and password edit boxes 
username_box = driver.find_element_by_id('form__username')
password_box = driver.find_element_by_id('form__password')
#enter in the username 
username_box.send_keys('warchief')
password_box.send_keys('sp1d3rman')

# find the login submit button 
log_in_submit = driver.find_element_by_css_selector('.text-right>input')
log_in_submit.click()







