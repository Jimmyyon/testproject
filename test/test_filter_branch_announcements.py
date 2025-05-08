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
        #進入所有公告
        anc=page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/span[2]')
        anc.wait_for(state='visible', timeout=10000)
        anc.click()
        #公告鈕
        #1.點開下拉
        page.locator('//div[contains(@class, "ant-select-selector")]').click()

        #2.點「台中克雷斯學校測試用分校」
        page.locator('//div[contains(@class, "ant-select-item-option-content") and text()="臺中克雷斯學校測試用分校"]').click()
        page.wait_for_timeout(5000)
    

        # #1.抓所有行 (所有的 div/div[i]/div[1])
        # elements = page.locator('/html/body/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/*/div[1]')

        # #2.取得所有行文字
        # texts = elements.all_inner_texts()

        # #3.預期值
        # expected_text = "臺中克雷斯學校測試用分校"

        # #4.assert 全部符合
        # assert all(text.strip() == expected_text for text in texts), f"有異常內容: {texts}"


        browser.close()
