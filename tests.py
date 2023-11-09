import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_name_length_less41_add_two_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_name_length_less41_no_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        # проверка, что у добавленной книги отсутствует жанр
        assert collector.get_books_genre()['Оно'] == ''

    def test_add_new_book_name_length_than40_not_added_book(self):
        collector = BooksCollector()

        collector.add_new_book('Новая длинная книга в «Сорок один символ»')
        # проверка, что название книги длиной 41 символ не запишется в словарь books_genre
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_existing_name_and_genre_add_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        # проверка, что существущий жанр в словаре genre запишется в словарь books_genre
        assert collector.get_books_genre()['Что делать, если ваш кот хочет вас убить'] == 'Детективы'

    def test_set_book_genre_existing_name_and_not_existing_genre_not_added_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Джон Уик')
        collector.set_book_genre('Джон Уик', 'Триллер')
        # проверка, что несуществущий жанр не запишется в словарь books_genre
        assert 'Триллер' not in collector.get_books_genre().values()

    def test_get_book_genre_existing_name_and_genre_getting_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        # проверка, что при получении жанра по существующей книге выдаст ее жанр
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Детективы'

    def test_get_book_genre_not_existing_name_none(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        # проверка, что при получении жанра по несуществующей книге выдаст None
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить 2') == None

    def test_get_books_with_specific_genre_existing_genre_add_book(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        # проверка, что в список books_with_specific_genre записалась книга, у которой жанр есть в списке genre
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_books_with_specific_genre('Детективы')

    def test_get_books_with_specific_genre_not_existing_genre_not_added_book(self):
        collector = BooksCollector()

        collector.add_new_book('Джон Уик')
        collector.set_book_genre('Джон Уик', 'Триллер')
        # проверка, что в список books_with_specific_genre не записалась книга с несуществующим жанром
        assert 'Джон Уик' not in collector.get_books_with_specific_genre('Триллер')

    def test_get_books_for_children_available_age_rating_add_book(self):
        collector = BooksCollector()

        collector.add_new_book('Приключение Незнайки')
        collector.set_book_genre('Приключение Незнайки', 'Мультфильмы')
        # проверям что в список books_for_children записалась книга
        assert 'Приключение Незнайки' in collector.get_books_for_children()

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Джон Уик', 'Триллер'],
            ['Оно', 'Ужасы']
        ]
    )
    def test_get_books_for_children_unavailable_age_rating_and_not_existing_genre_not_added_book(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверка, что в список books_for_children не добавилась книга
        assert name not in collector.get_books_for_children()

    def test_add_book_in_favorites_existing_name_and_name_not_favorites_add_book(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        # проверка, что в список favorites добавилась книга
        assert 'Оно' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_existing_name_not_added_book(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Джон Уик')
        # проверка, что в список favorites книга не добавилась
        assert 'Джон Уик' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_existing_name_and_name_is_favorites_not_added_book(self):
        collector = BooksCollector()
        collector.favorites = ['Оно']

        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        # проверка, что в список favorites книга не добавилась
        assert 'Оно' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', ['Оно', 'Оно 2'])
    def test_delete_book_from_favorites_existing_and_not_existing_name_del_book_from_favorites(self, name):
        collector = BooksCollector()
        collector.favorites = ['Оно', 'Приключение Незнайки']

        collector.add_new_book(name)
        collector.delete_book_from_favorites(name)
        # проверка, что в списке favorites отсутствуют тестовые данные
        assert name not in collector.get_list_of_favorites_books()
