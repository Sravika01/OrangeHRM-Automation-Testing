import datetime


def take_screenshot(driver, test_name):

    time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


    file_name = (
        "screenshots/"
        + test_name
        + "_"
        + time
        + ".png"
    )


    driver.save_screenshot(file_name)