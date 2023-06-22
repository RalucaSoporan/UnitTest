import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Dashboard(unittest.TestCase):

    def setUp(self):
        '''it contains all the steps that must be taken before class test time'''
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.chrome.implicitly_wait(15)

        self.chrome.find_element(By.XPATH, '//*[@name="username"]').send_keys('Admin')
        self.chrome.find_element(By.XPATH, '//*[@name="password"]').send_keys('admin123')
        self.chrome.find_element(By.XPATH, '//*[@type="submit"]').click()


    def test_time_at_work_is_displayed(self):
        '''The Time at work window is displayed'''
        time_at_work = self.chrome.find_element(By.XPATH, '//p[text() = "Time at Work"]')
        self.assertTrue(time_at_work.is_displayed(), True)

    def test_my_action_is_displayed(self):
        '''The My action window is displayed'''
        my_action = self.chrome.find_element(By.XPATH,'//*[text() = "My Actions"]')
        self.assertTrue(my_action.is_displayed(), True)


    def test_quick_launch_is_displayed(self):
        '''The Quick launch window is displayed'''
        quick_launch = self.chrome.find_element(By.XPATH, '//*[text() = "Quick Launch"]')
        self.assertTrue(quick_launch.is_displayed(), True)

    def test_buzz_latest_posts_is_displayed(self):
        '''The Buzz latest posts window is displaye'''
        buzz_latest_posts = self.chrome.find_element(By.XPATH, '//*[text() = "Buzz Latest Posts"]')
        self.assertTrue(buzz_latest_posts.is_displayed(), True)

    def test_employees_on_leave_today_is_displayed(self):
        '''The Employee on leave window is displaye'''
        employees_on_leave_today = self.chrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[5]/div/div[1]')
        self.assertTrue(employees_on_leave_today.is_displayed(), True)

    def test_employee_distribution_by_sub_unit_is_displayed(self):
        '''The Employee Distribution by Sub Unit window is display'''
        employee_distribution_by_sub_unit = self.chrome.find_element(By.XPATH, '//p[text() = "Employee Distribution by Sub Unit"]')
        self.assertTrue(employee_distribution_by_sub_unit.is_displayed(), True)

    def test_employee_distribution_by_location_is_displayed(self):
        '''The Employee Distribution by location window is display'''
        employee_distribution_by_location = self.chrome.find_element(By.XPATH, '//p[text() = "Employee Distribution by Location"]')
        self.assertTrue(employee_distribution_by_location.is_displayed(), True)


    def tearDown(self):
        '''All the activities that must be performed after any test in the respective class'''
        self.chrome.quit()
