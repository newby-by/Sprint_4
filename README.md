# The book collection application

## Acknowledgments

[The team of Yandex Practikum](https://github.com/yandex-praktikum)

Tomcat which gets up me early every morning.

## How to test

For testing we used the famous library `pytest`.

**Note**. See `requirements.txt` for detail.

### The check list

1. The tests for `add_new_book`.

    *Description.*
    ```
    Добавляет новую книгу в словарь без указания жанра. 
    Название книги может содержать максимум 40 символов. 
    Одну и ту же книгу можно добавить только один раз.
    ```

    - add 2 books with a unique name. The numbers `books_genre` increases on 2.

    **DONE**: test_add_new_book_add_two_books;

    - add a book with with a unique name. The value of `books_genre` is empty;
    - add a book with a existed `name`. The length of `books_genre` and the pair `(name, genre)` are not changed;
    - add a book with a name with 40 letters. The `books_genre` has the pair `(name, "")`;
    - add a book with a name with more 40 letters. The length of `books_genre` is not changed and and the pair `(name, "")` is not exists;
    - add a book with a name with 0 letters.
    The length of `books_genre` is not changed and and the pair `(name, "")` is not exists;

2. The tests for `set_book_genre`.

    *Description.*
    ```
    Устанавливает жанр книги, если книга есть в books_genre
    и её жанр входит в список genre.
    ```

    - a `genre` of an exist book can be set. The genre of the book is equal `genre`;
    - a `genre` of a non-existent book cannot be set. The exception is not raised;

3. The tests for `get_book_genre`.

    *Description.*
    ```
    Выводит жанр книги по её имени.
    ```

    - a `genre` of an exist book can be showed. The `genre` of the book is displayed;
    - set a non-existent name of a book. The exception is not raised;
    
4. The tests for `get_books_with_specific_genre`.

    *Description.*
    ```
    Выводит список книг с определённым жанром.
    ```

    - show all books with `genre`. Check a number of books and them names and genres;
    - show empty list for unused genre in books collection.

5. The tests for `get_books_genre`.

    *Description.*
    ```
    выводит текущий словарь books_genre.
    ```

    - show a list of genres. Compare with `['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']`;
  
6. The tests for `get_books_for_children`.

    *Description.*
    ```
    Возвращает книги, которые подходят детям. 
    У жанра книги не должно быть возрастного рейтинга.
    ```

7. The tests for `add_book_in_favorites`.

    *Description.*
    ```
    Добавляет книгу в избранное. 
    Книга должна находиться в словаре books_genre. 
    Повторно добавить книгу в избранное нельзя.
    ```

8. The tests for `delete_book_from_favorites`.

    *Description.*
    ```
    Удаляет книгу из избранного, если она там есть.
    ```

9. The tests for `get_list_of_favorites_books`.

    *Description.*
    ```
    Получает список избранных книг.
    ```

## Miscellaneous

1. Use VS Code exts:
    `code-spell-checker`
