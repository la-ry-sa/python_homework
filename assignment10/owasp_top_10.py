from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://owasp.org/www-project-top-ten/")
time.sleep(3)

risks = driver.find_elements(By.XPATH, "//li/a[starts-with(@href, 'https://owasp.org/Top10/')]/strong")

results = []

for risk in risks:
    title = risk.text.strip()
    link = risk.find_element(By.XPATH, "./parent::a").get_attribute("href").strip()
    results.append({"Title": title, "Link": link})

driver.quit()

for item in results:
    print(item)

df = pd.DataFrame(results)

df.to_csv("assignment10/risks.csv")