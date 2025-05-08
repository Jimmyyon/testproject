# login_page.py

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("xpath=/html/body/div/div/div/div/form/div[1]/div[1]/div[2]/div[1]/div/span/input")
        self.password_input = page.locator("xpath=/html/body/div/div/div/div/form/div[2]/div[1]/div[2]/div[1]/div/span/input")
        self.login_button = page.locator("xpath=/html/body/div/div/div/div/form/div[4]/div/div/div/div/div/div/button")
