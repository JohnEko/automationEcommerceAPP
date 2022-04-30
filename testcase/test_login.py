import pytest
from selenium import webdriver
from pageObjects.LoginTest import Login
from utillities.ReadProperties import Readconfig
from utillities.customLog import Loggen


class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    email = Readconfig.getEmail()
    password = Readconfig.getPassword()


    def test_homepage(self,  setDriver):
        self.driver = setDriver
        self.driver.get(self.baseURL)
        home_title = self.driver.title

        if home_title == "My account - My Store":
            assert True


    def test_login(self, setDriver):
        self.driver=setDriver
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)
        self.login.clickSignIn()
        self.login.setEmail(self.email)
        self.login.setPassword(self.password)
        self.login.clickSubmit()

        login_title = self.driver.title
        if login_title == "My Store":
            assert True



