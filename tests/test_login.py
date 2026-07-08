import time


from utilities.driver_setup import get_driver
from pages.login_page import LoginPage
from utilities.screenshot import take_screenshot




def test_login():

    driver = get_driver()

    driver.get(
        "https://opensource-demo.orangehrmlive.com/"
    )


    login = LoginPage(driver)


    login.enter_username("Admin")



    login.enter_password("admin123")


    login.click_login()


    time.sleep(5)


    try:

        assert "dashboard" in driver.current_url.lower()


    except:

        take_screenshot(
            driver,
            "login_failed"
        )

        raise


    driver.quit()