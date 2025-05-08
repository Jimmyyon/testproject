import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage  
from playwright.sync_api import sync_playwright, expect



#帳號登入失敗案例
def test_Login_Fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  #t=關閉視窗 f開啟視窗
        page = browser.new_page()
        page.goto("https://uat-school-system.weclass.com.tw/v2/jaouyang-dev#/login")

        login_page = LoginPage(page)

        # 你自己寫帳號密碼這邊
        login_page.username_input.fill("test_enterprise9990")
        login_page.password_input.fill("12345678")

        login_page.login_button.click()

       # 等待錯誤訊息出現
        page.wait_for_selector("xpath=/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/div/div")

        # 斷言pop密碼錯誤訊息
        error_message = page.locator("xpath=/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/div/div")
        expect(error_message).to_have_text("用戶名或密碼錯誤")
        

        browser.close()
