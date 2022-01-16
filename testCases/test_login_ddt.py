from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.get_application_url()
    path = ".\\testData\\LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info('******** Test Case 2 **********')
        self.logger.info('******** Validate the page title after logging in **********')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.get_row_count(self.path, 'Sheet1')
        print("total no of rows = ", self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.read_data(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.read_data(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.read_data(self.path, 'Sheet1', r, 3)
            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            #time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("************ Test Case passed ***********************")
                    self.lp.click_logout()
                    lst_status.append("Pass")

                elif self.exp == "Fail":
                    self.logger.info("************ Test Case failed ***********************")
                    self.lp.click_logout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("************ Test Case Failed ***********************")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("************ Test Case passed ***********************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("********** DDT passed ***********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** DDT Failed ***********")
            self.driver.close()
            assert False
        self.logger.info("------------ Testing Completed ---------------")