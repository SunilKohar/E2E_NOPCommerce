import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    lnk_customer_menu_xpath = "(//a[@href='#'])[7]"
    lnk_customer_menuitem_xpath = "//*[text()=' Customers']"
    lnk_add_new_xpath = "//a[@href='/Admin/Customer/Create']"
    txt_email_id = "Email"
    txt_password_name = "Password"
    txt_first_name = "FirstName"
    txt_last_name = "LastName"
    rd_gender_male_id = "Gender_Male"
    rd_gender_female_id = "Gender_Female"
    txt_dob_name = "DateOfBirth"
    txt_comapany_name = "Company"
    chkbox_tax_exempt_name = "IsTaxExempt"
    drpdwn_newsletter_name = "SelectedNewsletterSubscriptionStoreIds"
    txt_cusotmer_roles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    drpdwn_mgr_vendor_id = "VendorId"
    lstitem_administrators_xpath = "//li[text()='Administrators']"
    lstitem_forum_moderators_xpath = "//li[text()='Forum Moderators']"
    lstitem_guests_xpath = "//li[text()='Guests']"
    lstitem_registered_xpath = "//li[text()='Registered']"
    lstitem_vendors_xpath = "//li[text()='Vendors']"
    txt_admin_comment_name = "AdminComment"
    btn_save_name = "save"

    def __init__(self, driver):
        self.driver = driver

    def click_customer_menu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_xpath).click()

    def click_customer_menu_item(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menuitem_xpath).click()

    def click_add_new_button(self):
        self.driver.find_element(By.XPATH, self.lnk_add_new_xpath).click()

    def set_emailid(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def set_first_name(self, fname):
        self.driver.find_element(By.NAME, self.txt_first_name).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element(By.NAME, self.txt_last_name).send_keys(lname)

    def set_dateofbirth(self, dob):
        self.driver.find_element(By.NAME, self.txt_dob_name).send_keys(dob)

    def set_company(self, company):
        self.driver.find_element(By.NAME, self.txt_comapany_name).send_keys(company)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rd_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rd_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rd_gender_male_id).click()

    def set_tax_exempt(self,value):
        if value == 'yes':
            self.driver.find_element(By.NAME,self.chkbox_tax_exempt_name).click()

    def set_newsletter(self,value):
        drp = Select(self.driver.find_element(By.NAME, self.drpdwn_newsletter_name))
        drp.select_by_visible_text(value)

    def set_customer_role(self,role):
        self.driver.find_element(By.XPATH,self.txt_cusotmer_roles_xpath).click()
        time.sleep(2)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitem_registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_administrators_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_vendors_xpath)
        elif role == 'Guests':
            self.driver.find_element(By.XPATH,"//*[@aria-label='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_guests_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_forum_moderators_xpath)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def set_vendor_manager(self,value):
        drp = Select(self.driver.find_element(By.ID, self.drpdwn_mgr_vendor_id))
        drp.select_by_visible_text(value)

    def set_admin_comment(self, comment):
        self.driver.find_element(By.NAME, self.txt_admin_comment_name).send_keys(comment)

    def click_save(self):
        self.driver.find_element(By.NAME,self.btn_save_name).click()