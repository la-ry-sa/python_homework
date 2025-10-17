from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
time.sleep(3)

li_elements = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")

results = []

for li in li_elements:
    title = li.find_element(By.CSS_SELECTOR, "h3.cp-title span.title-content").text.strip()
    authors = "; ".join(
        a.text.strip() for a in li.find_elements(By.CSS_SELECTOR, "a.author-link")
    )
    format_year = li.find_element(By.CSS_SELECTOR, "div.cp-format-info span.display-info").text.strip()

    book = {
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    }
    results.append(book)

driver.quit()
df = pd.DataFrame(results)
print(df)

df.to_csv("assignment10/get_books.csv")

with open("assignment10/get_books.json", "w") as file:
    json.dump(results, file, indent=4)
