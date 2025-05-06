from behave import given
from playwright.sync_api import expect

@given('the user is on the homepage')
def step_user_on_homepage(context):
    page = context.page
    page.goto(context.base_url)
    expect(page).to_have_title("Läslistan")
