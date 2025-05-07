from playwright.sync_api import sync_playwright

# Called once before any tests run
def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)

# Called before every scenario (test case)
def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_url = "https://tap-ht24-testverktyg.github.io/exam-template/"

# Called after every scenario
def after_scenario(context, scenario):
    context.page.close()

# Called once after all tests are done
def after_all(context):
    context.browser.close()
    context.playwright.stop()
