import time
from behave import *

#behave features
@given(u'I navigate to google.com')
def step_impl(context):
    context.driver.get("http://www.google.com/")
    context.driver.implicitly_wait(5)


@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print("Title is :" + title)
    assert "Google" in title


@then(u'I enter the text Hello Selenium')
def step_impl(context):
    context.driver.find_element_by_name("q").send_keys("Hello Selenium")

@then(u'I click on search button')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
    time.sleep(3)


