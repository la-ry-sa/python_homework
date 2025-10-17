from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/Web_scraping")

from selenium.webdriver.common.by import By

title = driver.title # Find the title.  Parts of the header are accessed directly, not via find_element(), which only works on the body
print(title)

body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one
if body:
    links = body.find_elements(By.CSS_SELECTOR,'a') # Find all the links in the body.
    if len(links) > 0:
        print("href: ", links[0].get_attribute('href'))  # getting the value of an attribute



main_div = body.find_element(By.CSS_SELECTOR,'div[id="mw-content-text"]')
if main_div:
    bolds = main_div.find_elements(By.CSS_SELECTOR,'b')
    if len(bolds) > 0:
        print("bolds: ",bolds[0].text)

# Extract all images with their src attributes
images = [(img.get_attribute('src')) for img in body.find_elements(By.CSS_SELECTOR,'img[src]')] # all img elements with a src attribute
print("Image Sources:", images)
# hmm, this example uses a list comprehension.  We haven't talked about those.  This is the same as:
image_entries = driver.find_elements(By.CSS_SELECTOR,'img[src]')
images = []
for img in image_entries:
    images.append(img.get_attribute('src'))

print("Image Sources:", images)
# You can see that list comprehensions are a useful shortcut in Python!

driver.quit()