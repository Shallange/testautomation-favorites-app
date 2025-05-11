from behave import when, then
from pages.add_book_page import AddBookPage

@when('the user clicks the "Lägg till bok" button')
def step_click_add_book(context):
    context.add_page = AddBookPage(context.page)
    context.add_page.go_to_add_book_tab()

@when('enters "{title}" as the title')
def step_enter_title(context, title):
    context.add_page.enter_title(title)

@when('enters "{author}" as the author')
def step_enter_author(context, author):
    context.add_page.enter_author(author)

@then('the "Lägg till ny bok" button should become enabled')
def step_check_button_enabled(context):
    context.add_page.is_submit_enabled()

@then('the user clicks the "Lägg till ny bok" button')
def step_click_add_new_book(context):
    context.add_page.submit_book()

@then('the book "{title}" should appear in the "Katalog" tab')
def step_book_should_appear(context, title):
    context.add_page.assert_book_visible(title)


