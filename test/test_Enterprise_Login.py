import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage  
from dotenv import load_dotenv
load_dotenv()
ENTERPRISE_user = os.getenv("ENTERPRISE_USERNAME")
ENTERPRISE_pass = os.getenv("ENTERPRISE_PASSWORD")
TestURL = os.getenv("BASE_URL")

#企業登入
def test_Enterprise_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  #t=關閉視窗 f開啟視窗
        page = browser.new_page()
        page.goto(TestURL)

        login_page = LoginPage(page)

        #帳號密碼這邊
    
        login_page.username_input.fill(ENTERPRISE_user)
        login_page.password_input.fill(ENTERPRISE_pass)

        login_page.login_button.click()

        page.wait_for_timeout(3000)  # 等待頁面載入
        

        browser.close()
