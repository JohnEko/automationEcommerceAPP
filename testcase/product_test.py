import pytest
from selenium import webdriver
from pageObjects.LoginTest import Login
from pageObjects.ProductTest import Product
from utillities.ReadProperties import Readconfig
from utillities.customLog import Loggen

class Test_Product_002:
    baseURL = Readconfig.getApplicationURL()
    email = Readconfig.getEmail()
    password = Readconfig.getPassword()
    logger = Loggen.logger()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_products(self, setDriver):
        #self.logger.info("*************Test_Product_002***************")
        self.driver = setDriver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        page_title =self.driver.title
        if page_title == "My Store":
            assert True

        else:
            assert "The store is not found"


    @pytest.mark.regression
    def test_loginProduct(self, setDriver):
        #it will get the loginpage
        #self.logger.info("*****************Login page***********")
        self.driver = setDriver
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)
        self.login.clickSignIn()
        self.login.setEmail(self.email)
        self.login.setPassword(self.password)
        self.login.clickSubmit()

       #The will get the product page
        self.checkprod = Product(self.driver)
        self.checkprod.clickOnProductmenu()
        self.checkprod.clickOnDressMenu()
        #self.driver.close()
        #self.logger.info("*****************Check Product page**************")


        self.checkprod.clickOntops()
        self.checkprod.clickOnAboutUs()
        product_title = self.driver.title

        if product_title == "Top quality products":
            assert True

        else:
            assert "Products id not found"

        #self.logger.info("*****************Test Completed**************")