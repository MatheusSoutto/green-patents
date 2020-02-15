from selenium import webdriver
from selenium.webdriver.common.keys import Keys

proxyString = "spica.eic.cefet-rj.br:8085"

desired_capability = webdriver.DesiredCapabilities.FIREFOX
desired_capability['proxy'] = {
    "proxyType": "manual",
    "httpProxy": proxyString,
    "ftpProxy": proxyString,
    "sslProxy": proxyString
}

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
profile.set_preference('app.update.enabled', False)
profile.set_preference('app.update.auto', False)
profile.set_preference('app.update.service.enabled', False)
#profile.set_preference('app.update.staging.enabled', False)
#profile.set_preference('app.update.silent', False)
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile, capabilities=desired_capability, executable_path=r"C:\Users\MatheusdeAbreuGoncal\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe")

alert = driver.switch_to.alert
alert.send_keys("44878904895" + Keys.TAB + "44878904895")
alert.accept()

driver.switch_to.window(driver.window_handles[0])
driver.maximize_window()

driver.get("https://www.periodicos.capes.gov.br/")

driver.find_element_by_xpath(".//button[text()='Fechar']").click()


#################### END ######################

driver.quit()