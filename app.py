from chalice import Chalice
from selenium import webdriver
import time, os

app = Chalice(app_name='chalice-selenium-chrome-headless-demo')

@app.route('/')
def index():
    driver = web_driver()
    driver.get("https://robertorocha.info/setting-up-a-selenium-web-scraper-on-aws-lambda-with-python/")
    time.sleep(5)
    src = driver.page_source
    driver.close()
    return { "html": str(src) }

def web_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument("--enable-javascript")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    chrome_options.binary_location = "/opt/bin/headless-chromium"
    return webdriver.Chrome(chrome_options=chrome_options)