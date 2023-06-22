import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Menu_aplication(unittest.TestCase):
    USERNAME = (By.XPATH, '//*[@name="username"]')
    PASSWORD = (By.XPATH, '//*[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@type="submit"]')
    MENU_LIST = (By.CLASS_NAME, 'oxd-sidepanel-body')
    ADMIN = (By.LINK_TEXT, 'Admin')
    PIM = (By.LINK_TEXT, 'PIM')
    LEAVE = (By.LINK_TEXT, 'Leave')

    def setUp(self):
        '''it contains all the steps that must be taken before class test time'''
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.chrome.implicitly_wait(15)

        self.chrome.find_element(*self.USERNAME).send_keys('Admin')
        self.chrome.find_element(*self.PASSWORD).send_keys('admin123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()


    def test_identification_list_menu_admin(self):
        '''I check if there is an Admin window in the menu list'''
        menu_list = self.chrome.find_element(*self.MENU_LIST).text
        admin = self.chrome.find_element(*self.ADMIN).text
        self.assertIn(admin,menu_list, f'{menu_list}, {admin}')
        print(menu_list)
        print(admin)

    def test_pim_in_menu_list(self):
        '''I check if there is an PIM window in the menu list'''
        menu_list = self.chrome.find_element(*self.MENU_LIST).text
        pim = self.chrome.find_element(*self.PIM).text
        self.assertIn(pim,menu_list)

    def test_leave_in_menu(self):
        '''I check if there is an Leave window in the menu list'''
        menu_list = self.chrome.find_element(*self.MENU_LIST).text
        leave = self.chrome.find_element(*self.LEAVE).text
        self.assertIn(leave,menu_list, f'{leave}, {menu_list}')



    def tearDown(self):
        '''All the activities that must be performed after any test in the respective class'''
        self.chrome.quit()


