import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_page(unittest.TestCase):


    USERNAME = (By.XPATH, '//*[@name="username"]')
    PASSWORD = (By.XPATH, '//*[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@type="submit"]')
    LOGO_TITLE = (By.XPATH, '//*[@alt="company-branding"]')
    LOGIN_TITLE= (By.XPATH, '//h5')
    INVALID_CREDENTIALS = (By.XPATH, '//*[text() = "Invalid credentials"]')

    def setUp(self):
        '''It contains all the steps that must be taken before class test time'''
        self.chrome = webdriver.Chrome()
        self.chrome.implicitly_wait(5)
        self.chrome.maximize_window()
        self.chrome.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    def test_logo_page(self):
        '''I checked if the logo appears on the page'''
        title = self.chrome.find_element(*self.LOGO_TITLE)
        actual = title.is_displayed()
        self.assertTrue(actual, True)

    def test_text_page_title(self):
        '''I checked the page title'''
        title = self.chrome.find_element(*self.LOGIN_TITLE)
        expected = 'Login'
        actual = title.text
        self.assertEqual(expected,actual)



    def test_login_page_with_user_name_incorrect_and_password_correct(self):
        '''I checked if I can log in with an incorrect username and the correct password
        error displayed
        '''
        self.chrome.find_element(*self.USERNAME).send_keys('incorrect_username')
        self.chrome.find_element(*self.PASSWORD).send_keys('admin123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(3)
        expected = 'Invalid credentials'
        actual = self.chrome.find_element(*self.INVALID_CREDENTIALS).text
        self.assertEqual(expected, actual)



    def test_login_page_with_user_name_correct_and_password_incorrect(self):
        '''I checked if I can log in with an correct username and the incorrect password,
         error displayed
         '''
        self.chrome.find_element(*self.USERNAME).send_keys('Admin')
        self.chrome.find_element(*self.PASSWORD).send_keys('password_invalid')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected = 'Invalid credentials'
        actual = self.chrome.find_element(*self.INVALID_CREDENTIALS).text
        self.assertEqual(expected, actual)

    def test_login_page_with_user_name_correct_and_password_none(self):
        '''I checked if I can log in with the correct username and missing password,
        error displayed
        '''
        self.chrome.find_element(*self.USERNAME).send_keys('Admin')
        self.chrome.find_element(*self.PASSWORD).send_keys('')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected = 'Required'
        actual = self.chrome.find_element(By.XPATH, '//span[text() = "Required"]').text
        self.assertEqual(expected, actual)


    def test_login_page_with_user_name_none_and_password_correct(self):
        '''I checked if I can log in with the missing username and correct password
        error displayed
        '''
        self.chrome.find_element(*self.USERNAME).send_keys('')
        self.chrome.find_element(*self.PASSWORD).send_keys('admin123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected = 'Required'
        actual = self.chrome.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span').text
        self.assertEqual(expected, actual)

    def test_login_page_with_user_name_correct_and_password_correct(self):
        '''I tried to log in with the correct credentials'''
        self.chrome.find_element(*self.USERNAME).send_keys('Admin')
        self.chrome.find_element(*self.PASSWORD).send_keys('admin123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)


    def tearDown(self):
        '''All the activities that must be performed after any test in the respective class'''
        self.chrome.quit()



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

    def test_search_button_with_invalid_texy(self):
        '''Enter an invalid text in the search box and I check if they stay on the same page'''
        self.chrome.find_element(*self.SEARCH_BUTTON).send_keys('@#$%')
        expected = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        actuat = self.chrome.current_url
        self.assertEqual(expected,actuat)

    def tearDown(self):
        '''All the activities that must be performed after any test in the respective class'''
        self.chrome.quit()

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



