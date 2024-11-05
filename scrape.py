from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.headless = True
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.javascript": 2})
driver = webdriver.Chrome(options=options)

hero_names = ["Cassidy"]

try: 
  driver.get("https://www.overbuff.com/heroes?role=damage")

  WebDriverWait(driver, 20).until(
      EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Cassidy')]"))
  )

  for name in hero_names:
    name_element = driver.find_element(By.XPATH, f"//a[contains(text(), '{name}')]")
    root_element = name_element.find_element(By.XPATH, ".//ancestor::tr[1]")
    win_rate_bar_element = root_element.find_element(By.XPATH, f".//descendant::div[contains(@class, 'bg-stat-win')]")
    win_rate_element = win_rate_bar_element.find_element(By.XPATH, ".//ancestor::td[1]/descendant::span[contains(text(), '.')]")
    win_rate = win_rate_element.text

    print(f"{name} win rate: {win_rate}")

finally:
  driver.quit()