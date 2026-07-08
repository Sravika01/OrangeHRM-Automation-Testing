from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeePage:


    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver,10)


    def click_pim(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//span[text()='PIM']")
            )
        ).click()


    def click_add_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT,"Add Employee")
            )
        ).click()


    def enter_employee_details(self):

        self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME,"firstName")
            )
        ).send_keys("John")


        self.driver.find_element(
            By.NAME,
            "lastName"
        ).send_keys("Smith")


    def save_employee(self):

        self.driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        ).click()