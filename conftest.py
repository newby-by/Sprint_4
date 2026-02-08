import pytest

from data import (
    book_name_adult_one,
    book_name_adult_two,
    book_name_child_one,
    book_name_child_two,
    book_name_child_three,
    genres_adult,
    genres_child
)
from main import BooksCollector


@pytest.fixture
def child_genres():
    yield genres_child


@pytest.fixture
def collector():
    collector = BooksCollector()
    yield collector
    del collector


@pytest.fixture
def some_name_book():
    yield book_name_adult_one


@pytest.fixture
def another_name_book():
    yield book_name_adult_two


@pytest.fixture
def collector_with_book(collector):
    collector.add_new_book(book_name_adult_one)
    yield collector


@pytest.fixture
def collector_with_book_and_genre(collector_with_book,
                                  some_name_book):
    collector_with_book.set_book_genre(some_name_book, genres_adult[0])
    yield collector_with_book


@pytest.fixture
def genre(collector_with_book_and_genre, some_name_book):
    genre = collector_with_book_and_genre.get_books_genre().get(
        some_name_book
    )
    yield genre


@pytest.fixture
def collector_with_two_adult_books(collector_with_book_and_genre,
                                   another_name_book):
    collector_with_book_and_genre.add_new_book(another_name_book)
    collector_with_book_and_genre.set_book_genre(
        another_name_book, genres_adult[1]
    )

    yield collector_with_book_and_genre


@pytest.fixture
def list_adult_book_names(collector_with_two_adult_books):
    books = collector_with_two_adult_books.get_books_genre()
    list_adult_books_name = [book for book, genre in books.items()
                             if genre in genres_adult]

    yield list_adult_books_name


@pytest.fixture
def collector_with_full_type_genre_books(collector_with_two_adult_books,
                                         child_genres):
    collector_with_two_adult_books.add_new_book(book_name_child_one)
    collector_with_two_adult_books.set_book_genre(book_name_child_one,
                                                  child_genres[0])
    collector_with_two_adult_books.add_new_book(book_name_child_two)
    collector_with_two_adult_books.set_book_genre(book_name_child_two,
                                                  child_genres[1])
    collector_with_two_adult_books.add_new_book(book_name_child_three)
    collector_with_two_adult_books.set_book_genre(book_name_child_three,
                                                  child_genres[2])

    yield collector_with_two_adult_books


@pytest.fixture
def list_child_book_names(collector_with_full_type_genre_books, child_genres):
    books = collector_with_full_type_genre_books.get_books_genre()
    list_child_books_name = [book for book, genre in books.items()
                             if genre in child_genres]

    yield list_child_books_name


@pytest.fixture
def collector_with_favorites(collector_with_full_type_genre_books,
                             list_adult_book_names,
                             list_child_book_names):
    collector_with_full_type_genre_books.add_book_in_favorites(
        list_adult_book_names[0]
    )
    collector_with_full_type_genre_books.add_book_in_favorites(
        list_child_book_names[0]
    )
    yield collector_with_full_type_genre_books


@pytest.fixture
def list_favorites(collector_with_full_type_genre_books):
    yield collector_with_full_type_genre_books.favorites
