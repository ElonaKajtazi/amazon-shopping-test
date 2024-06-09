
from behave import given, when, then
from pages.amazon_home_page import AmazonHomePage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

@given('I am on the Amazon home page')
def step_impl(context):
    context.page.goto('https://www.amazon.com')

@when('I search for "{product_name}"')
def step_impl(context, product_name):
    amazon_home_page = AmazonHomePage(context.page)
    amazon_home_page.search_for_product(product_name)

@when('I select the first product')
def step_impl(context):
    product_page = ProductPage(context.page)
    product_page.select_first_product()

@when('I add the product to the basket')
def step_impl(context):
    product_page = ProductPage(context.page)
    product_page.add_to_basket()

@then('the basket count should be "{count}"')
def step_impl(context, count):
    amazon_home_page = AmazonHomePage(context.page)
    assert amazon_home_page.get_cart_count() == count

@when('I go to the basket')
def step_impl(context):
    basket_page = BasketPage(context.page)
    basket_page.go_to_basket()


@when('I update the quantity to "{quantity}"')
def step_impl(context, quantity):
    basket_page = BasketPage(context.page)
    basket_page.update_quantity(quantity)
    context.page.reload()

@then('the basket count should now be "{count}"')
def step_impl(context, count):
    amazon_home_page = AmazonHomePage(context.page)
    context.page.wait_for_timeout(2000)  
    actual_count = amazon_home_page.get_cart_count()
    assert actual_count == count
