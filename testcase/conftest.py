import pytest
from selenium import webdriver



@pytest.fixture
def setDriver():
    driver=webdriver.Chrome()
    return driver

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'e commerce shop' #the project name
    config._metadata['Module Name'] = 'Client'  #what you are working on
    config._metadata['Tester'] = 'Efe'  #Tester name


#This is hooks on delete or modify Environment info to HTML Rport
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Javascript_home", None)
    metadata.pop("Plugin", None)