from playwright.sync_api import Page

class AmazonHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = page.locator('input#twotabsearchtextbox')
        self.search_button = page.locator('input#nav-search-submit-button')
        self.cart_icon = page.locator('#nav-cart-count')


    def load(self):
        self.page.goto('https://www.amazon.com')

    def search_for_product(self, product_name: str):
        self.search_box.fill(product_name)
        self.search_button.click()
    
    def get_cart_count(self):
        return self.cart_icon.inner_text()