import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage  
from dotenv import load_dotenv
load_dotenv()

corp_user = os.getenv("ENTERPRISE_USERNAME")
corp_pass = os.getenv("ENTERPRISE_PASSWORD")

#確認總覽功能正常
def test_Staff_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  #t=關閉視窗 f開啟視窗
        page = browser.new_page()
        page.goto("https://uat-school-system.weclass.com.tw/v2/jaouyang-dev#/login")

        login_page = LoginPage(page)

        #帳號密碼這邊
    
        login_page.username_input.fill(corp_user)
        login_page.password_input.fill(corp_pass)

        login_page.login_button.click()

        page.wait_for_timeout(3000)  # 等待頁面載入
        #分別去點擊其他item
        dashboard=page.locator('xpath=/html/body/div/div/div/div[2]/div[1]/ul/li[2]/span')
        dashboard.click()
        get_branch_student_attendance_rate=page.locator('xpath=/html/body/div/div/div/div[2]/div[1]/ul/li[3]')
        get_branch_student_attendance_rate.click()
        get_class_student_attendance_rate=page.locator('xpath=/html/body/div/div/div/div[2]/div[1]/ul/li[4]/span')
        get_class_student_attendance_rate.click()
        #返回總覽
        overviews=page.locator('xpath=/html/body/div/div/div/div[2]/div[1]/ul/li[1]/span')
        overviews.click()
        assert page.locator('xpath=/html/body/div/div/div/div[2]/div[1]/ul/li[1]/span').is_visible()

       
       

        browser.close()
