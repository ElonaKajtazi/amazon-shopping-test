from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_product = page.locator('[data-cy="title-recipe"]').first
        self.add_to_basket_button = page.locator('input#add-to-cart-button')
        

    def select_first_product(self):
        self.first_product.click()

    def add_to_basket(self):
        self.add_to_basket_button.click()