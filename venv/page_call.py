from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time , json
from waity import wait_time

weblog = webdriver.Chrome()
weblog.get("https://identity.qa-hitpa.consint.ai/realms/eo2v2/protocol/openid-connect/auth?client_id=eo2m2_hitpa_client&redirect_uri=https%3A%2F%2Fqa-hitpa.consint.ai%2F&state=da7a79bc-03ac-4ce8-98fc-b6051d5aec6a&response_mode=fragment&response_type=code&scope=openid&nonce=46651907-33cf-47af-84c4-d9191c5a3404&code_challenge=13_3ZxSeLmTRe2HgEeYHdVl8OsWnZ12J1a6yi8Ko8mI&code_challenge_method=S256")
# LOGIN
username = wait_time(weblog,By.ID,"username").send_keys("div_check")
password = wait_time(weblog,By.ID,"password").send_keys("Welcome@123")
submit = wait_time(weblog,By.NAME,"login").click()

otp = int(input("write otp for login>"))

otp_fill = wait_time(weblog,By.ID,"otp").send_keys(otp)
sign_in = wait_time(weblog,By.ID,"kc-login").click()

print("login success")
weblog.maximize_window()
weblog.execute_script("document.body.style.zoom='67%'")

time.sleep(4)


menu = wait_time(weblog,By.XPATH,'//button[.//*[contains(@data-testid,"MenuIcon")]]').click()
claim = WebDriverWait(weblog,20).until(
    EC.element_to_be_clickable(
        (By.XPATH,"//div[@role='button'][.//span[normalize-space()='Claim Management']]")
    )
)
claim.click()

time.sleep(10)











