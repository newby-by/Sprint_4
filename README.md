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

        **SKIP**: `test_add_new_book_add_two_books`

    - add a book with a unique name. The value of `books_genre` is not changed;

        **DONE**: `test_add_new_book_with_unique_name`

    - add a book with a name with 40 letters. The `books_genre` has the pair `(name, "")`;

        **TODO**

    - add a name of a book with with more 40 letters. The length of `books_genre` is not changed and and the pair `(name, "")` is not exists;

        **DONE**: `test_add_new_book_with_name_more_40_letters`

    - add a book with a name with 0 letters. The length of `books_genre` is not changed and and the pair `(name, "")` is not exists;

2. The tests for `set_book_genre`.

    *Description.*
    ```
    Устанавливает жанр книги, если книга есть в books_genre
    и её жанр входит в список genre.
    ```

    - a `genre` of an exist book can be set. The genre of the book is equal `genre`;

        **DONE**: `test_set_book_genre_for_exits_book`

    - a `genre` of a non-existent book cannot be set. `books_genre` is not changed;

3. The tests for `get_book_genre`.

    *Description.*
    ```
    Выводит жанр книги по её имени.
    ```

    - a `genre` of an exist book can be showed. The `genre` of the book is displayed;

        **DONE**: `test_get_book_genre_for_exist_book`

    - set a non-existent name of a book. The exception is not raised;

4. The tests for `get_books_with_specific_genre`.

    *Description.*
    ```
    Выводит список книг с определённым жанром.
    ```

    - show all books with `genre`. Check a list of books;

        **DONE**: `test_get_books_with_specific_genre_exist_books_with_genre`

    - show empty list for unused genre in books collection.

5. The tests for `get_books_genre`.

    *Description.*
    ```
    Выводит текущий словарь books_genre.
    ```
    - show a list of `books_genres`. Check type of a result object is dict. Contains correct data.

        **DONE**: `test_get_books_genre_unempty_list_books`
  
6. The tests for `get_books_for_children`.

    *Description.*
    ```
    Возвращает книги, которые подходят детям. 
    У жанра книги не должно быть возрастного рейтинга.
    ```

    - show all books for children. Check a number of books and them names and genres are not in the list `['Ужасы', 'Детективы']`;
  
        **DONE**: `test_get_books_for_children_unempty_list_books`

    - show empty list of books for children if books are genres in `['Ужасы', 'Детективы']` only.

7. The tests for `add_book_in_favorites`.

    *Description.*

    ```
    Добавляет книгу в избранное. 
    Книга должна находиться в словаре books_genre. 
    Повторно добавить книгу в избранное нельзя.
    ```

    - add a unique name of a book that is in `books_genre` and `favorites` is empty. The length of `favorites` increases on 1. The name of a book is in `favorites`.

        **DONE**: `test_add_book_in_favorites_with_unique_name_and_favorites_is_empty`

    - add a unique name of a book that is in `books_genre` and `favorites` is not empty. The length of `favorites` increases on 1. The name of a book is in `favorites`.
    - add a name of a book with a unique name in `favorites`. The length of `favorites` is not changed.

8. The tests for `delete_book_from_favorites`.

    *Description.*

    ```
    Удаляет книгу из избранного, если она там есть.
    ```

    - remove a name of a book that is in `favorites`. The `favorites` decreases on 1. The name of a book is not in `favorites`.
  
    **DONE**: `test_delete_book_from_favorites_with_exist_name`

    - remove a name of a book that is not in `favorites`. The length of `favorites` is not changed.
  
9. The tests for `get_list_of_favorites_books`.

    *Description.*

    ```
    Получает список избранных книг.
    ```

    - show a list of `favorites` that is not empty. The list of names contains actual data: the length and names.

    **DONE**: `test_get_list_of_favorites_books_with_unempty_favorites`

    - show a list of `favorites` that is empty. The list of names contains `[]`.

## Miscellaneous

1. Use VS Code exts:
    `code-spell-checker`
