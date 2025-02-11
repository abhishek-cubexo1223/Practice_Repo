from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (AppiumBy.ID, "com.example:id/username")
        self.password_field = (AppiumBy.ID, "com.example:id/password")
        self.login_button = (AppiumBy.ID, "com.example:id/login")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
