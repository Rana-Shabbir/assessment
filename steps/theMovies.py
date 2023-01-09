from behave import *
from appium import webdriver
import time

desired_cap = {
    "deviceName": "R58R72TBP2B",
    "platformName": "Android",
    "appPackage": "com.mobile_app.themovie",
    "appActivity": "com.mobile_app.themovie.presentation.ui.main_menu.MainMenuActivity",
    "app": "C:\\Users\\rana\\Desktop\\mobile_automation\\TheMovie_1.4_Apkpure.apk",
    "newCommandTimeout": 8000
}


@given('Launch TheMovie - Application')
def launchApp(context):
    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    context.driver.implicitly_wait(30)


@then('Verify the application logo.')
def verifyLogo(context):
    context.driver.find_element("id", "com.mobile_app.themovie:id/logo").is_displayed()


