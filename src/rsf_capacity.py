from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

url = 'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e'

def getChrome():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-dev-shm-usage')
    chrome = webdriver.Chrome(executable_path='../chromedriver', options=opt)
    chrome.get(url)
    return chrome


def getCapacity(chrome):
    try:
        capacity = WebDriverWait(chrome, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]/div[2]/div/span"))
        )
        capacity_text = capacity.text
    finally:
        return capacity_text
