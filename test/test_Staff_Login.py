import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage 
from dotenv import load_dotenv



emp_user = os.getenv("EMPLYOEE_USERNAME")
emp_pass = os.getenv("EMPLYOEE_PASSWORD")

#職員登入
def test_login_with_real_account():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  #t=關閉視窗 f開啟視窗
        page = browser.new_page()
        page.goto("https://uat-school-system.weclass.com.tw/v2/jaouyang-dev#/login")

        login_page = LoginPage(page)

    
        #帳號開始登入輸入帳號與密碼
        login_page.username_input.fill(emp_user)
        login_page.password_input.fill(emp_pass)

        login_page.login_button.click()

        page.wait_for_timeout(3000)  # 等待頁面載入
        

        browser.close()
