class Login:
    sign_in  = "//a[@class='login']"
    email_input_id = "email"
    password_input_id = "passwd"
    click_submitButton = "SubmitLogin"


    def __init__(self, driver):
        self.driver = driver

    def clickSignIn(self):
        self.driver.find_element_by_xpath(self.sign_in).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.email_input_id).clear()
        self.driver.find_element_by_id(self.email_input_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_input_id).clear()
        self.driver.find_element_by_id(self.password_input_id).send_keys(password)

    def clickSubmit(self):
        self.driver.find_element_by_id(self.click_submitButton).click()