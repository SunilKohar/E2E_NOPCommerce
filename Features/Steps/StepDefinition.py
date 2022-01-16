from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

@given(u'User Opens the browser, enters the URL')
def step_impl(context):
    path = 'H:\\Drivers\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)
    context.driver.get("https://admin-demo.nopcommerce.com/login")


@when(u'I have user credentials and log in')
def step_impl(context):
    context.driver.find_element(By.NAME, "Email").clear()
    context.driver.find_element(By.NAME, "Email").send_keys('admin@yourstore.com')
    context.driver.find_element(By.NAME, "Password").clear()
    context.driver.find_element(By.NAME, "Password").send_keys('admin')
    context.driver.find_element(By.XPATH, "//*[text()='Log in']").click()


@when(u'I click on the customer side bar')
def step_impl(context):
    print("i clicked on customer button from sidebar")


@when(u'I click on the Add button to add customer details')
def step_impl(context):
    print("I click on the Add button to add customer details")


@then(u'I verify that the customer has been added successfully')
def step_impl(context):
    print("I verify that the customer has been added successfully")
