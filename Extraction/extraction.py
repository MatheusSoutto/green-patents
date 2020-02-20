from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

############################ CONFIGURAÇÃO PROXY ############################

proxyString = "spica.eic.cefet-rj.br:8085"

desired_capability = webdriver.DesiredCapabilities.FIREFOX
desired_capability['proxy'] = {
    "proxyType": "manual",
    "httpProxy": proxyString,
    "ftpProxy": proxyString,
    "sslProxy": proxyString
}

############################ CONFIGURAÇÃO PROFILE ############################

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
profile.set_preference('app.update.enabled', False)
profile.set_preference('app.update.auto', False)
profile.set_preference('app.update.service.enabled', False)
#profile.set_preference('app.update.staging.enabled', False)
#profile.set_preference('app.update.silent', False)
profile.update_preferences()

############################ INÍCIO DRIVER ############################

driver = webdriver.Firefox(firefox_profile=profile, capabilities=desired_capability, executable_path=r"C:\Users\MatheusdeAbreuGoncal\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe")

try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = driver.switch_to.alert
    alert.send_keys("44878904895" + Keys.TAB + "44878904895")
    alert.accept()

    driver.switch_to.window(driver.window_handles[0])
    print("alert accepted")
except TimeoutException:
    print("no alert")

driver.maximize_window()

driver.get("https://www.periodicos.capes.gov.br/")

driver.find_element_by_xpath(".//a[text()='Buscar base']").click()

tab1 = driver.window_handles[0]

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

driver.find_element_by_id("scan_start").send_keys("Derwent")

driver.find_element_by_xpath(".//input[@value='Enviar']").click()

driver.find_element_by_xpath(".//a[contains(text(), 'Derwent Innovations Index')]").click()


#################### END ######################

driver.quit()