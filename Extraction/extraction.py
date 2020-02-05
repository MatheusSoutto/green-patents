from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\MatheusdeAbreuGoncal\Downloads\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.periodicos.capes.gov.br/")

driver.find_element_by_xpath(".//button[text()='Fechar']").click()

#################### SELECT INSTITUTION ######################

driver.find_element_by_class_name("chosen-single").click()

driver.find_element_by_xpath(".//div[@class='chosen-search']/input").send_keys('uff' + Keys.ENTER)

driver.find_element_by_id("enviarInstituicaoCafe").click()

#################### LOGIN FORM ######################

driver.find_element_by_id("username").send_keys("01444990535")

driver.find_element_by_id("password").send_keys("metodologia")

driver.find_element_by_xpath(".//button[@type='submit']").click()


#################### END ######################

driver.quit()