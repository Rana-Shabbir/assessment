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


@then('Get text of select tv label & Verify Screen Title.')
def getTvName(context):
    tvLabelName = context.driver.find_element("id", "com.mobile_app.themovie:id/tv_movie").text

    context.driver.find_element("id", "com.mobile_app.themovie:id/tv_movie").click()
    time.sleep(2)

    if tvLabelName == "Movies":
        assert True
        print("Expected tv name is Correct")
    else:
        print("Expected tv name is Incorrect")
        assert False


@then('Tap on the selected movie.')
def tapSelectedMovie(context):
    context.driver.find_element("xpath",
                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/f.d"
                                ".e.a[1]/android.widget.RelativeLayout/android.widget.TextView[2]").click()
    time.sleep(7)


@then('Verify Expected tv name is Correct or Incorrect.')
def verifySelectMovieName(context):
    selectedMovieName = context.driver.find_element("id", "com.mobile_app.themovie:id/ad_tv_title").text

    if selectedMovieName == "Avatar: The Way of Water":
        print("Expect movie name is correct")
        assert True
    else:
        print("Expect movie name is incorrect")
        assert False

