import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Search_button(unittest.TestCase):
    def setUp(self):
        '''it contains all the steps that must be taken before class test time'''
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.chrome.implicitly_wait(15)

        self.chrome.find_element(By.XPATH, '//*[@name="username"]').send_keys('Admin')
        self.chrome.find_element(By.XPATH, '//*[@name="password"]').send_keys('admin123')
        self.chrome.find_element(By.XPATH, '//*[@type="submit"]').click()

    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[placeholder="Search"]')

    def test_search_button_is_displayed(self):
        '''The search button is displayed'''
        search_button =self.chrome.find_element(*self.SEARCH_BUTTON)
        self.assertTrue(search_button.is_displayed(), True)

    def test_search_button_with_valid_text(self):
        '''Enter a valid text in the search box and enter the page found'''
        self.chrome.find_element(*self.SEARCH_BUTTON).send_keys('My info')
        self.chrome.find_element(By.LINK_TEXT, "My Info").click()
        expected = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"
        actual = self.chrome.current_url
        self.assertEqual(expected,actual)

    def test_search_button_with_invalid_text(self):
        '''Enter an invalid text in the search box and I check if they stay on the same page'''
        self.chrome.find_element(*self.SEARCH_BUTTON).send_keys('@#$%')
        expected = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        actuat = self.chrome.current_url
        self.assertEqual(expected,actuat)

    def tearDown(self):
        '''All the activities that must be performed after any test in the respective class'''
        self.chrome.quit()