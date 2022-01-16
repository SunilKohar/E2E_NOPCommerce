from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Add_Customer_page import AddCustomer
import random
import string


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_003_Add_Customer:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_add_customer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("********* Login Successfull **********")
        self.logger.info("******** start Adding new customer *******")

        self.addcust= AddCustomer(self.driver)
        self.addcust.click_customer_menu()
        self.addcust.click_customer_menu_item()
        self.addcust.click_add_new_button()

        self.logger.info("******** Provide customer details ***********")
        self.email = random_generator() + "@getnada.com"
        self.addcust.set_emailid(self.email)
        self.addcust.set_password("passwerr123")
        self.addcust.set_first_name("test")
        self.addcust.set_last_name("123")
        self.addcust.set_gender("Female")
        self.addcust.set_dateofbirth("03/06/1986")
        self.addcust.set_company("ABS Corps")
        #self.addcust.set_newsletter("Your store name")
        self.addcust.set_customer_role("Guests")
        #self.addcust.set_vendor_manager("Vendor 2")
        self.addcust.set_admin_comment("tmdhjmbfdvj,bhf,mvb ,jn,nhvmhbd vsbv m svb")
        self.addcust.click_save()

        self.msg = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            print("Test case passed")
            assert True == True
        else:
            assert True == False

        self.driver.close()