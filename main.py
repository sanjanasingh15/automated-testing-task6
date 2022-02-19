import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

os.environ['PATH'] += r";C:\Selenium-Drivers"
driver = webdriver.Chrome()
driver.get("https://www.thesparksfoundationsingapore.org/")
driver.maximize_window()

# Testcase 1 - Title
print('Testcase 1:')
element1 = driver.title
if element1:
    print(element1)
    if (element1 == 'The Sparks Foundation | Home'):
        print('The title is present and correct\n')
    else:
        print('The title is present but incorrect\n')
else:
    print('Title is not available\n')

# Testcase 2 - Navigation Bar
print('Testcase 2:')
try:
    driver.find_element(By.CSS_SELECTOR, 'nav')
    print('Navigation Bar is present\n')
except NoSuchElementException:
    print('Navigation Bar is unavailable\n')

# Testcase 3 - About Us/Vision, Mission and Values page
print('Testcase 3:')
try:
    driver.find_element(By.LINK_TEXT, 'About Us').click()
    time.sleep(1)
    try:
        driver.find_element(By.LINK_TEXT, 'Vision, Mission and Values').click()
        print('Vision, Mission and Values page in About Us section is available.\n')
    except NoSuchElementException:
        print('Vision, Mission and Values page in About Us section is unavailable\n')
except NoSuchElementException:
    print('About Us section is unavailable\n')

time.sleep(2)

# Testcase 4 - Policies and Code/Personal Data Policy page
print('Testcase 4:')
try:
    driver.find_element(By.LINK_TEXT, 'Policies and Code').click()
    time.sleep(1)
    try:
        driver.find_element(By.LINK_TEXT, 'Personal Data Policy').click()
        print('Personal Data Policy page in Policies and Code section is available.\n')
    except NoSuchElementException:
        print('Personal Data Policy page in Policies and Code section is unavailable\n')
except NoSuchElementException:
    print('Policies and Code section is unavailable\n')

time.sleep(2)

# Testcase 5 - Programs/Workshops page
print('Testcase 5:')
try:
    driver.find_element(By.LINK_TEXT, 'Programs').click()
    time.sleep(1)
    try:
        driver.find_element(By.LINK_TEXT, 'Workshops').click()
        print('Workshops page in Programs section is available.\n')
    except NoSuchElementException:
        print('Workshops page in Programs section is unavailable\n')
except NoSuchElementException:
    print('Programs section is unavailable\n')

time.sleep(2)

# Testcase 6 - Links/Salient Features page
print('Testcase 6:')
try:
    driver.find_element(By.LINK_TEXT, 'LINKS').click()
    time.sleep(1)
    try:
        driver.find_element(By.LINK_TEXT, 'Salient Features').click()
        print('Salient Features page in LINKS section is available.\n')
    except NoSuchElementException:
        print('Salient Features page in LINKS section is unavailable\n')
except NoSuchElementException:
    print('Links section is unavailable\n')

time.sleep(2)

# Testcase 7 - Join Us/Why Join Us page
print('Testcase 7:')
try:
    driver.find_element(By.LINK_TEXT, 'Join Us').click()
    time.sleep(1)
    try:
        driver.find_element(By.LINK_TEXT, 'Why Join Us').click()
        print('Why Join Us page in Join Us section is available.\n')
    except NoSuchElementException:
        print('Why Join Us page in Join Us section is unavailable\n')
except NoSuchElementException:
    print('Join Us section is unavailable\n')

time.sleep(2)

# Testcase 8 - Logo
print('Testcase 8:')
try:
    value = driver.find_element(By.XPATH, "//img[@src='/images/logo_small.png']")
    if value:
        print('Logo is present\n')
except NoSuchElementException:
    print('Logo is unavailable\n')

time.sleep(2)

# Testcase 9 - Home Link
print('Testcase 9:')
try:
    driver.find_element(By.XPATH, "//a[@class='col-md-6 navbar-brand']").click()
    print('Home Link is working\n')
    time.sleep(1)
except NoSuchElementException:
    print('Home Link is unavailable\n')

time.sleep(2)

# Testcase 10 - Slider Element
print('Testcase 10:')
try:
    driver.find_element(By.LINK_TEXT, "4").click()
    print('Slider Item 4 is present\n')
    time.sleep(1)
except NoSuchElementException:
    print('Slider Item 4 is unavailable\n')

time.sleep(2)

# Testcase 11 - Facebook Link
print('Testcase 11:')
try:
    element = driver.find_element(By.XPATH, "//i[@class='fa fa-facebook']")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)
    element.click()
    print('Facebook link is present and working\n')
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
except NoSuchElementException:
    print('Facebook link is unavailable\n')

time.sleep(2)

# Testcase 12 - Scroll To Top
print('Testcase 12:')
try:
    driver.find_element(By.ID, 'toTopHover').click()
    time.sleep(1)
    print('Scroll to Top button is present and working\n')
except NoSuchElementException:
    print('Scroll to Top button is unavailable\n')

time.sleep(2)

driver.quit()
