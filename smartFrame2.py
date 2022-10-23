from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# //prepare
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
smartFrame2 = driver.get('https://smartitnow.blogspot.com/p/w.html')
driver.maximize_window()
driver.find_element(By.ID,'cookieChoiceDismiss').click()

# // find & test it
photo = driver.find_element(By.ID, 'post-body-4144740677389794309')
photo = ActionChains(driver) \
    .move_to_element(photo)\
    .perform()
shareButtonVisible = driver.find_element(By.CSS_SELECTOR, 'smart-frame  a.action-buttons__button.--share')
if shareButtonVisible.is_displayed():
    print('OK: Share button is visible')
else:
    print('FAIL: Share button is not visible')
driver.find_element(By.CSS_SELECTOR, 'smart-frame  a.action-buttons__button.--custom').click()
current_window_name = driver.current_window_handle
window_name = driver.window_handles
for window in window_name:
    if window != current_window_name:
        driver.switch_to.window(window)
print(driver.current_url)

if driver.current_url != smartFrame2:
    print('OK: Redirect work')
else:
    print('FAIL: Redirect is not working')
driver.quit()
