from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# //prepare
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://smartitnow.blogspot.com/p/e.html')
driver.maximize_window()
driver.find_element(By.ID,'cookieChoiceDismiss').click()

# // find & test it
photo = driver.find_element(By.ID, 'post-body-2195234803014015561')
photo = ActionChains(driver) \
    .move_to_element(photo)\
    .perform()
iframe = driver.find_element(By.CSS_SELECTOR, '#post-body-2195234803014015561 > iframe')
driver.switch_to.frame(iframe)
captionVisible = driver.find_element(By.CSS_SELECTOR, 'div.main.active  div.caption-box ')
if captionVisible.is_displayed():
    print('OK: Caption is visible')
else:
    print('FAIL: Caption is not visible')
driver.find_element(By.CSS_SELECTOR, 'a.--embed').click()
layerOpen = driver.find_element(By.CSS_SELECTOR, 'div.mobile.hide-copyright.active')
if layerOpen.is_displayed():
    print('OK: Layer is visible')
else:
    print('FAIL: Layer is not visible')
driver.quit()



