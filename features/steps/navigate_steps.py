from behave import when, then
from playwright.sync_api import expect

@when('the user clicks the "{tab}" tab')
def step_click_tab(context, tab):
    page = context.page
    tab_map = {
        "Katalog": "catalog",
        "Mina böcker": "favorites",
        "Lägg till bok": "add-book"
    }
    button = page.get_by_test_id(tab_map[tab])
    if not button.is_disabled(): #ensuring it does not try to click on an already active tab 
        button.click()


@then('the content for "{tab}" should be shown')
def step_check_tab_content(context, tab):
    page = context.page
    if tab == "Katalog":
        expect(page.locator("div.catalog")).to_be_visible()
    elif tab == "Mina böcker":
        expect(page.locator("div.favorites")).to_be_visible()
    elif tab == "Lägg till bok":
        expect(page.get_by_test_id("add-submit")).to_be_visible()
