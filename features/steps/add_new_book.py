from behave import when, then
from playwright.sync_api import expect

@when('the user clicks the "Lägg till bok" button')
def step_click_add_book(context):
    page = context.page
    add_book_button = page.get_by_test_id("add-book")
    expect(add_book_button).to_be_enabled()
    add_book_button.click()

@when('enters "{title}" as the title')
def step_enter_title(context, title):
    page = context.page
    title_input = page.get_by_test_id("add-input-title")
    title_input.fill(title)

@when('enters "{author}" as the author')
def step_enter_author(context, author):
    page = context.page
    author_input = page.get_by_test_id("add-input-author")
    author_input.fill(author)

@then('the "Lägg till ny bok" button should become enabled')
def step_check_button_enabled(context):
    page = context.page
    submit_button = page.get_by_test_id("add-submit")
    expect(submit_button).to_be_enabled()

@then('the user clicks the "Lägg till ny bok" button')
def step_click_add_new_book(context):
    page = context.page
    submit_button = page.get_by_test_id("add-submit")
    submit_button.click()

@then('the book "{title}" should appear in the "Katalog" tab')
def step_book_should_appear(context, title):
    page = context.page
    katalog_button = page.get_by_test_id("catalog")
    katalog_button.click()
    expect(page.get_by_text(title)).to_be_visible()


