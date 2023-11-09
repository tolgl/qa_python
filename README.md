# qa_python
1. Тест __test_add_new_book_name_length_less41_add_two_book__ проверяет добавление двух книг в словарь books_genre с количеством сиволов в названии менее 41
2. Тест __test_add_new_book_name_length_less41_no_genre__ проверяет, что у добавленной книги в словарь books_genre отсутствует жанр
3. Тест __test_add_new_book_name_length_than40_not_added_book__ проверяет, что при добавлении книги в словарь books_genre с количеством символов более 40 книга не записывается
4. Тест __test_set_book_genre_existing_name_and_genre_add_genre__ проверяет, что существующий жанр в списке genre добавится к книге в словаре books_genre
5. Тест __test_set_book_genre_existing_name_and_not_existing_genre_not_added_genre__ проверяется, что отсутсвующий жанр в списке genre не добавится в словарь books_genre
5. Тест __test_get_book_genre_existing_name_and_genre_getting_genre__ проверяет, что по книге, которая есть в словаре books_genre, выдаст ее жанр
6. Тест __test_get_book_genre_not_existing_name_none__ проверяет, что при получении жанра по книге, которая отсутствует в словаре books_genre, метод выдаст значение None
7. Тест __test_get_books_with_specific_genre_existing_genre_add_book__ проверяет, что в список books_with_specific_genre записалась книга, у которой жанр есть в списке genre
8. Тест __test_get_books_with_specific_genre_not_existing_genre_not_added_book__ проверяет, что в список books_with_specific_genre не записалась книга с отсутсвующим жанром в списке genre
9. Тест __test_get_books_for_children_available_age_rating_add_book__ проверяет, что книга с жанром из списка genre добавилась в список books_for_children
10. Тест __test_get_books_for_children_unavailable_age_rating_and_not_existing_genre_not_added_book__ проверяет, что книга с жанром из списка genre_age_rating и с несуществующим жанром не записывается в список books_for_children
11. Тест __test_add_book_in_favorites_existing_name_and_name_not_favorites_add_book__ проверяет, что книга, которая есть в словаре books_genre и которая отсутствует в списке favorites, добавилась в список favorites
12. Тест __test_add_book_in_favorites_not_existing_name_not_added_book__ проверяет, что книга, которая отсутствует в словаре books_genre, не добавилась в список favorites
13. Тест __test_add_book_in_favorites_existing_name_and_name_is_favorites_not_added_book__ проверяет, что книга, которая уже есть в списке favorites, не добавилась снова в список favorites
14. Тест __test_delete_book_from_favorites_existing_and_not_existing_name_del_book_from_favorites__ проверяет, что книга, которая есть в списке favorites и которой нет в списке favorites, после удаления отсутствует в списке favorites 