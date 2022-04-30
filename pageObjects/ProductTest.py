from selenium.webdriver.support.ui import Select

class Product:

    linkProduct_xpath_click = "//a[contains(text(),'Women')]"
    linkDresses_xpath = "//a[@class='subcategory-name']"
    btn_id = "layered_id_attribute_group_13"
    link_product_menu = "//a[contains(text(),'About us')]"



    def __init__(self, driver):
        self.driver= driver

    def clickOnProductmenu(self):
        self.driver.find_element_by_xpath(self.linkProduct_xpath_click).click()

    def clickOnDressMenu(self):
        self.driver.find_element_by_xpath(self.linkDresses_xpath).click()

    def clickOntops(self):
        self.driver.find_element_by_id(self.btn_id).click()

    def clickOnAboutUs(self):
        self.driver.find_element_by_xpath(self.link_product_menu).click()

