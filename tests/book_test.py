from pages.book_page import BookPage


class TestBookPage:

    def test_book(self, browser):
        book_page = BookPage(browser, "http://localhost:3000/main")
        book_page.open()
        book_page.create_booking()

