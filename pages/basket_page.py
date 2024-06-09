from playwright.sync_api import Page

class BasketPage:
    def __init__(self, page: Page):
        self.page = page
        self.basket_button = page.locator('a#nav-cart')
        self.quantity_dropdown = page.locator('select[name="quantity"]')
        # # self.quantity_dropdown = page.locator('[data-a-class="quantity"]')
        # self.quantity_option = page.locator(f'#quantity_{quantity}')


    def go_to_basket(self):
        self.basket_button.click()

    def update_quantity(self, quantity: int):
        self.quantity_dropdown.select_option(str(quantity))
    
    def get_basket_count(self):
        return self.page.inner_text('span#nav-cart-count')

        
