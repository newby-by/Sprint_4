import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.skip
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_with_unique_name(self):
        """Add a book with a unique name."""
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        expected_books_genre = collector.get_books_genre()
        
        collector.add_new_book(name)

        assert collector.get_books_genre() == expected_books_genre
