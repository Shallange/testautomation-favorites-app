from behave import when, then
from playwright.sync_api import expect

@when('the user returns to the "Katalog" tab')
def step_return_to_catalog(context):
    page = context.page
    katalog_button = page.get_by_test_id("catalog")
    katalog_button.click()

@when('the user clicks the heart icon for the book "Min katt är min chef" again')
def step_click_heart_again(context):
    page = context.page
    heart = page.get_by_test_id("star-Min katt är min chef")
    heart.click()
    expect(heart).not_to_have_class("selected")

@then('the book "Min katt är min chef" should no longer appear in the "Mina böcker" tab')
def step_book_should_not_be_in_favorites(context):
    page = context.page
    favorites_tab = page.get_by_test_id("favorites")
    favorites_tab.click()
    expect(page.get_by_text("Min katt är min chef")).not_to_be_visible()
