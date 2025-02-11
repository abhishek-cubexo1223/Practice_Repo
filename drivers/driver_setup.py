from appium import webdriver

def get_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": "https://bx-bb-mobile-wrappers.s3.amazonaws.com/590444/master/0.5.7_Android_release.apk",
        "automationName": "UiAutomator2"
    }
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
