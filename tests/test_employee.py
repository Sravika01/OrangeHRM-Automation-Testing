import time

from utilities.driver_setup import get_driver

from pages.login_page import LoginPage

from pages.employee_page import EmployeePage


def test_add_employee():


    driver = get_driver()


    driver.get(
        "https://opensource-demo.orangehrmlive.com/"
    )


    login = LoginPage(driver)


    login.enter_username("Admin")

    login.enter_password("admin123")

    login.click_login()


    employee = EmployeePage(driver)


    employee.click_pim()


    employee.click_add_employee()


    employee.enter_employee_details()


    employee.save_employee()


    time.sleep(5)


    print("Employee Added Successfully")


    input("Press ENTER to close")


    driver.quit()