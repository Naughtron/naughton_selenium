#imports
import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

# create a new class for the test 

class SearchForGame(unittest.TestCase):

	# create setup
	def setUp(self):
		self.driver = webdriver.Firefox()

	# create the test
	def test_search_for_game_on_gb(self):
		driver = self.driver
		# address
		driver.get("http://www.giantbomb.com")
		# assert you are on the correct site
		self.assertIn("Giant Bomb", driver.title)
		# find the search box
		search_box = driver.find_element_by_name('q')
		# enter in search text 
		search_box.send_keys('Ratchet and Clank')
		# hit return 
		search_box.send_keys(Keys.RETURN)
		# assert one of the results that comes back
		self.assertTrue('Ratchet & Clank Future: A Crack in Time')
		
	# tear down
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()

