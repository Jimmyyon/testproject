import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage  
from playwright.sync_api import sync_playwright, expect
from dotenv import load_dotenv
load_dotenv()
ENTERPRISE_user = os.getenv("ENTERPRISE_USERNAME")
ENTERPRISE_pass = os.getenv("ENTERPRISE_PASSWORD")
TestURL = os.getenv("BASE_URL")

#最新公告顯示正常
def test_bulletin_content():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(TestURL)

        login_page = LoginPage(page)

        
        
        #帳號開始登入輸入帳號與密碼
        login_page.username_input.fill(ENTERPRISE_user)
        login_page.password_input.fill(ENTERPRISE_pass)
        login_page.login_button.click()

        page.wait_for_timeout(7000)  # 等待登入後頁面載入

        # 等待頁面加載完畢，特別是跳轉後的元素
        page.wait_for_selector('xpath=/html/body/div/div/div/div[1]/ul/li[1]', timeout=10000)

        # 首頁籤文字是否正確
        tab = page.locator('xpath=/html/body/div/div/div/div[1]/ul/li[1]')
        assert tab.inner_text() == "個人中心", f"Expected '個人中心', but got {tab.inner_text()}"
        tab.click()
        #進入最新公告
        page.wait_for_selector('xpath=/html/body/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]', timeout=10000)
        news =page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/span[1]')
        assert news.inner_text() =="最新公告"
        #點擊所有公告並且印出內容
        page.wait_for_selector('xpath=/html/body/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]', timeout=10000)
        allnews =page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/span[2]')
        allnews.click()


        page.wait_for_timeout(20000)  # 等待登入後頁面載入
        page.wait_for_selector('xpath=/html/body/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div', timeout=10000)
        firstnews_element= page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div')
        firstnews = firstnews_element.inner_text()
        print(f"\n目前公告內容為：{firstnews}")