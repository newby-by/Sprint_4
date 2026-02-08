from copy import deepcopy

import pytest

from data import (LENGTH_NAME_MORE_40_LETTERS_41,
                  LENGTH_NAME_MORE_40_LETTERS_45)
from data import (
    book_name_adult_one,
    book_name_adult_two,
    book_name_child_one,
    book_name_child_two,
    book_name_child_three,
    genres_adult,
    genres_child
)

class TestBooksCollector:

    def test_add_new_book_add_two_books(self,
                                        collector,
                                        another_name_book):
        collector.add_new_book(book_name_adult_one)
        collector.add_new_book(another_name_book)

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_with_unique_name(self, collector):
        """Add a book with a unique name."""
        expected_books_genre = {book_name_adult_one: ''}
        collector.add_new_book(book_name_adult_one)

        assert collector.get_books_genre() == expected_books_genre

    @pytest.mark.parametrize(
            'name_length_more_40',
            [
                LENGTH_NAME_MORE_40_LETTERS_41,
                LENGTH_NAME_MORE_40_LETTERS_45,
            ]
    )
    def test_add_new_book_with_name_more_40_letters(self,
                                                    collector,
                                                    name_length_more_40):
        """Add name of a book with more 40 letters."""
        expected_books_genre = deepcopy(collector.get_books_genre())
        name = 'A' * name_length_more_40

        collector.add_new_book(name)

        assert collector.get_books_genre() == expected_books_genre

    def test_set_book_genre_for_exist_book(self,
                                           collector_with_book):
        """A genre of an exist book can be set."""
        expected_genre_book = genres_adult[0]
        expected_name_book = list(collector_with_book.get_books_genre())[0]

        collector_with_book.set_book_genre(expected_name_book,
                                           expected_genre_book)

        actual_genre_book = collector_with_book.get_books_genre().get(
            expected_name_book
        )
        assert actual_genre_book == expected_genre_book

    def test_get_book_genre_for_exist_book(self,
                                           collector_with_book_and_genre,
                                           genre):
        """A genre of an exist book can be displayed."""
        actual_genre = collector_with_book_and_genre.get_book_genre(
            book_name_adult_one
        )

        assert actual_genre == genre

    def test_get_books_with_specific_genre_exist_books_with_genre(
            self,
            collector_with_book_and_genre
    ):
        """Show all exist books with genre."""
        genre_comedy = 'Комедии'
        expected_books_name = 'Что делать, если ваш кот хочет вас убить'

        collector_with_book_and_genre.add_new_book(expected_books_name)
        collector_with_book_and_genre.set_book_genre(expected_books_name,
                                                     genre_comedy)

        actual_books_name = (collector_with_book_and_genre.
                             get_books_with_specific_genre(genre_comedy)[0])

        assert actual_books_name == expected_books_name

    def test_get_books_genre_unempty_list_books(
            self,
            collector_with_book_and_genre,
            genre,
    ):
        """Show unempty dict of books_genres."""
        actual_books_genre = collector_with_book_and_genre.get_books_genre()

        assert (isinstance(actual_books_genre, dict) and
                actual_books_genre == {book_name_adult_one: genre})

    def test_get_books_for_children_unempty_list_books(
            self,
            collector_with_full_type_genre_books,
            list_child_book_names
    ):
        """Show all books for children."""
        actual_child_books = (collector_with_full_type_genre_books.
                              get_books_for_children())
        assert (len(actual_child_books) == len(list_child_book_names) and
                list_child_book_names[0] in actual_child_books and
                list_child_book_names[1] in actual_child_books and
                list_child_book_names[2] in actual_child_books)

    def test_add_book_in_favorites_with_unique_name_favorites_is_empty(
            self,
            collector_with_full_type_genre_books
    ):
        """Add a unique name of a book that is in books_genre."""
        length_favorites = len(collector_with_full_type_genre_books.
                               get_list_of_favorites_books())

        expected_favorite_book = list(collector_with_full_type_genre_books.
                                      get_books_genre())[0]
        collector_with_full_type_genre_books.add_book_in_favorites(
            expected_favorite_book
        )

        actual_length_favorites = len(collector_with_full_type_genre_books.
                                      get_list_of_favorites_books())
        actual_favorites = (collector_with_full_type_genre_books.
                            get_list_of_favorites_books())

        assert (actual_length_favorites == length_favorites + 1 and
                expected_favorite_book in actual_favorites)

    def test_delete_book_from_favorites_with_exist_name(
            self,
            collector_with_favorites,
            list_favorites):
        """Remove an exist name of a book that is in favorites."""
        favorites_length = len(list_favorites)
        expected_favorite_book = list_favorites[0]
        collector_with_favorites.delete_book_from_favorites(list_favorites[0])

        assert (len(collector_with_favorites.get_list_of_favorites_books()) ==
                favorites_length - 1 and
                expected_favorite_book not in
                collector_with_favorites.get_list_of_favorites_books())

    def test_get_list_of_favorites_books_with_unempty_favorites(
            self,
            collector_with_favorites,
            list_favorites):
        """Show a unempty list of favorites that is not empty."""
        actual_favorites = (collector_with_favorites.
                            get_list_of_favorites_books())
        assert (len(actual_favorites) == len(list_favorites) and
                actual_favorites == list_favorites)
