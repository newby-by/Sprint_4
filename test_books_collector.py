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

    def test_set_book_genre_for_exist_book(self):
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

    def test_get_books_with_specific_genre_exist_books_with_genre(self):
        """Show all exist books with genre."""
        collector = BooksCollector()
        genre = 'Ужасы'
        expected_movies_names = [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        ]
       
        collector.add_new_book(expected_movies_names[0])
        collector.set_book_genre(expected_movies_names[0], genre)
        collector.add_new_book(expected_movies_names[1])
        collector.set_book_genre(expected_movies_names[1], genre)

        actual_movie_names = collector.get_books_with_specific_genre(genre)

        assert actual_movie_names == expected_movies_names

    def test_get_books_genre_unempty_list_books(self):
        """Show unempty dict of books_genres."""
        collector = BooksCollector()
        expected_books_genre = {
            'Гордость и предубеждение и зомби': '',
            'Что делать, если ваш кот хочет вас убить': '',
        }
        collector.add_new_book(list(expected_books_genre)[0])
        collector.add_new_book(list(expected_books_genre)[1])

        actual_books_genre = collector.get_books_genre()

        assert (isinstance(actual_books_genre, dict) and 
                actual_books_genre == expected_books_genre)

    def test_get_books_for_children_unempty_list_books(self):
        """Show all books for children."""
        collector = BooksCollector()
        expected_movies_names_for_adult = [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        ]
        collector.add_new_book(expected_movies_names_for_adult[0])
        collector.set_book_genre(expected_movies_names_for_adult[0], 'Ужасы')
        collector.add_new_book(expected_movies_names_for_adult[1])
        collector.set_book_genre(expected_movies_names_for_adult[1], 'Детективы')

        expected_movies_names_for_child = [
            'ОНО',
            'Пила 6',
            'Сайлент хилл',
        ]
        collector.add_new_book(expected_movies_names_for_child[0])
        collector.set_book_genre(expected_movies_names_for_child[0], 'Фантастика')
        collector.add_new_book(expected_movies_names_for_child[1])
        collector.set_book_genre(expected_movies_names_for_child[1], 'Мультфильмы')
        collector.add_new_book(expected_movies_names_for_child[2])
        collector.set_book_genre(expected_movies_names_for_child[2], 'Комедии')

        assert collector.get_books_for_children() == expected_movies_names_for_child

    def test_add_book_in_favorites_with_unique_name_and_favorites_is_empty(self):
        """Add a unique name of a book that is in books_genre."""
        collector = BooksCollector()
        expected_favorites_length = len(collector.favorites)
        expected_favorite_movie_name = 'ОНО'
        collector.add_new_book('Гордость и предубеждение и зомби',)
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book(expected_favorite_movie_name)
        collector.set_book_genre(expected_favorite_movie_name, 'Комедии')

        collector.add_book_in_favorites(expected_favorite_movie_name)

        assert (len(collector.get_list_of_favorites_books()) == 
                expected_favorites_length + 1 and
                expected_favorite_movie_name in 
                collector.get_list_of_favorites_books())
