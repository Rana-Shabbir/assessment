# yassir-assessment
QA coding challenge

Appium Basic Demo for Behave (BDD)
These are sample test cases for The movie and general usage that can get you familiar with Appium.

BDD framework used is Behave which is an Cucumber clone for Python.

Mobile Test Automation framework is Appium which is most supported right now.

Install Behave and Appium:

pip install appium-python-client
pip install behave

**Usage:
**
# In order to execute your test script
~ behave 

# In order to prepare report run this cmd
~ behave -f allure_behave.formatter:AllureFormatter -o reports/

# In order to get report 
~ allure serve reports/
