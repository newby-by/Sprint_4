from copy import deepcopy

import pytest

from main import BooksCollector


class TestBooksCollector:
    LENGTH_NAME_MORE_40_LETTERS = 41

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
        expected_books_genre = deepcopy(collector.get_books_genre())
        
        collector.add_new_book(name)

        assert collector.get_books_genre() == expected_books_genre

    def test_add_new_book_with_name_more_40_letters(self):
        """Add name of a book with more 40 letters."""
        collector = BooksCollector()
        expected_books_genre = deepcopy(collector.get_books_genre())
        name = 'A' * self.LENGTH_NAME_MORE_40_LETTERS
        
        collector.add_new_book(name)

        assert collector.get_books_genre() == expected_books_genre

    def test_set_book_genre_for_exits_book(self):
        """A genre of an exist book can be set."""
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        expected_genre = 'Ужасы'

        collector.set_book_genre(name, expected_genre)

        assert collector.get_books_genre().get(name) == expected_genre

    def test_get_book_genre_for_exist_book(self):
        """A genre of an exist book can be displayed."""
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        expected_genre = 'Ужасы'
        collector.set_book_genre(name, expected_genre)

        actual_genre = collector.get_book_genre(name)

        assert actual_genre == expected_genre
