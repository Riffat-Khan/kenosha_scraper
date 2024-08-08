from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.headless = True

url = 'https://www.kenosha.org/building-permit-search'

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

form = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'addressRangeSearch'))
)

house_number1 = form.find_element(By.ID, 'arHouseNumber')
house_number1.send_keys('1234')
house_range_start = house_number1.get_attribute('outerHTML')

house_number2 = form.find_element(By.ID, 'arHouseNumber2')
house_number2.send_keys('5678')
house_range_end = house_number2.get_attribute('outerHTML')

street_name = form.find_element(By.ID, 'arStreetName')
street_name.send_keys('54th')
streed_name_content = street_name.get_attribute('outerHTML')

street_type = form.find_element(By.XPATH, './/select[@class="form-control"]')
select = Select(street_type)
select.select_by_visible_text('Street')

search_button_locator = (By.CSS_SELECTOR, '#addressRangeSearch .form-group input[type="button"][value="Search"]')
search_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(search_button_locator))
driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
search_button.click()

time.sleep(5) 

result_locator = (By.CSS_SELECTOR, '.assessment-row.form-horizontal')
results = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(result_locator))

for result in results:
    print(result.get_attribute('outerHTML'))
    
driver.quit()