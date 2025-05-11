from playwright.sync_api import expect

class AddBookPage:
    def __init__(self, page):
        self.page = page
        self.add_book_button = page.get_by_test_id("add-book")
        self.title_input = page.get_by_test_id("add-input-title")
        self.author_input = page.get_by_test_id("add-input-author")
        self.submit_button = page.get_by_test_id("add-submit")
        self.catalog_tab = page.get_by_test_id("catalog")

    def go_to_add_book_tab(self):
        expect(self.add_book_button).to_be_enabled()
        self.add_book_button.click()

    def enter_title(self, title):
        self.title_input.fill(title)

    def enter_author(self, author):
        self.author_input.fill(author)

    def is_submit_enabled(self):
        expect(self.submit_button).to_be_enabled()

    def submit_book(self):
        self.submit_button.click()

    def assert_book_visible(self, title):
        self.catalog_tab.click()
        expect(self.page.get_by_text(title)).to_be_visible()