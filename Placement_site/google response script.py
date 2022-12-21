from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def google_form_submit(url):
      
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    entries = soup.find_all("span",{"class":"NPEfkd RveJvd snByac"})
    # result_count = driver.find_element(By.CLASS_NAME, "NPEfkd RveJvd snByac").text
    print(entries)
    for e in entries:
        if e.text=="Submit":
            print(e)
            # e.submit()

url="https://docs.google.com/forms/d/e/1FAIpQLSdGIHxreezgi0LOmQfYqf4-lZdCEQ1B9vFEngXWRmUpkT8qYQ/viewform"
google_form_submit(url)