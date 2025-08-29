import time
from selenium.webdriver.common.by import By

def test_two_monitors(driver):
    driver.get('https://demoblaze.com/index.html')
    monitor_link = driver.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(2)
    monitors = driver.find_elements(By.CSS_SELECTOR, value = '.card')
    assert len(monitors) == 2



def test_open_s6(driver):
    driver.get('https://demoblaze.com/index.html')
    galaxy_s6 = driver.find_element(By.XPATH, value="//a[contains(text(),'Samsung galaxy s6')]")
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, value="h2")
    assert title.text == "Samsung galaxy s6"