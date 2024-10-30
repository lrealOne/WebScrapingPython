import pandas as pd;
import time
from selenium import webdriver as wd;
from selenium.webdriver.chrome.service import Service;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
print("ok service")
browser = wd.Chrome(service=service)
print("ok browser")
browser.get("https://www.google.com")
search_bar = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#APjFqb'))
)
print("ok busca")
user_search = input("Pesquise:")
search_bar.send_keys(user_search)
search_bar.send_keys(Keys.ENTER)

time.sleep(500)

