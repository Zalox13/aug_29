import time
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    #   driver.get('https://demoblaze.com/index.html')
    #   galaxy_s6 = driver.find_element(By.XPATH, value="//a[contains(text(),'Samsung galaxy s6')]")
    #   galaxy_s6.click()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung Galaxy S6')
    #    title = driver.find_element(By.CSS_SELECTOR, value="h2")
    #    assert title.text == "Samsung galaxy s6"

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    #    driver.get('https://demoblaze.com/index.html')
    homepage.click_monitor()
    #    monitor_link = driver.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    #    monitor_link.click()
    time.sleep(2)
    homepage.check_that_products_count(2)
    #    monitors = driver.find_elements(By.CSS_SELECTOR, value = '.card')
    #    assert len(monitors) == 2