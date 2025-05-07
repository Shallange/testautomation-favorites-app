from behave import given, when, then
from playwright.sync_api import expect

@given('the user is on the homepage')
def step_user_on_homepage(context):
    page = context.page
    page.goto(context.base_url)
    expect(page).to_have_title("Läslistan")

@when('the user hovers over the book "Min katt är min chef"')
# Shared hover step for favorite/unfavorite tests
def step_hover_book(context):
    page = context.page
    heart = page.get_by_test_id("star-Min katt är min chef")
    heart.hover()
    expect(heart).to_be_visible()

@when('the user clicks the heart icon for the book "Min katt är min chef"')
# Shared click heart step for favoriting/unfavoriting
def step_click_heart(context):
    page = context.page
    heart = page.get_by_test_id("star-Min katt är min chef")
    heart.click()
    expect(heart).to_have_class("star selected")

@then('the book "Min katt är min chef" should appear in the "Mina böcker" tab')
# Verifies the book appears in the favorites tab after favoriting
def step_book_should_be_in_favorites(context):
    page = context.page
    favorites_tab = page.get_by_test_id("favorites")
    favorites_tab.click()
    expect(page.get_by_text("Min katt är min chef")).to_be_visible()
