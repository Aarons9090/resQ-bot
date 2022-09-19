import time
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CONFIG = dotenv_values(".env")
EMAIL = CONFIG["EMAIL"]
PASSWORD = CONFIG["PASSWORD"]

OFFER_TO_FIND = "Insert offer here"


def main():

    opt = Options()
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.geolocation": 1,
    })

    driver = webdriver.Chrome(options=opt)
    driver.get('https://resq-club.com/app/')

    # log user in
    time.sleep(2)
    driver.find_element(By.ID, "profileButton").click()

    driver.find_element(By.ID, "input_email").send_keys(EMAIL)

    driver.find_element(By.ID, "input_password").send_keys(PASSWORD)
    driver.find_element(By.ID, "input_password").send_keys(Keys.ENTER)

    time.sleep(1)

    # click my location button to center map around user
    driver.find_element(By.CSS_SELECTOR, "#bigMapContainer > img").click()

    found = False
    while not found:
        offers = driver.find_elements(By.CLASS_NAME, "offerRow")
        print("searching...")
        for o in offers:
            try:
                # search for the index of the wanted item
                if o.text.find(OFFER_TO_FIND) != -1:
                    print("Found ", OFFER_TO_FIND)
                    found = True
                    # click on offer
                    o.click()

                    # click continue
                    driver.find_element(By.CSS_SELECTOR, "#mainContent > div:nth-child(4) > button").click()
                    time.sleep(0.5)

                    # click on the confirmation to order item
                    driver.find_element(By.CSS_SELECTOR, "#mainContent > div > button").click()
            except Exception as e:
                print(e)
        if not found:
            print(time.strftime("%H:%M:%S", time.localtime()), "not found")
        time.sleep(2)


if __name__ == '__main__':
    main()
