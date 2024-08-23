from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Проверка добавления книг с названиями в 1 символ, 22 и 40
    @pytest.mark.parametrize('name', ['Ъ', 'Путешествие во времени', 'Смешное летнее приключение Анабеллы Смит'])
    def test_add_new_book_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''

    # Устанавливаем книге жанр фантастика
    def test_set_book_genre_fantasy(self):
        collector = BooksCollector()
        name = 'Квантовый прыжок'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    # Получаем жанр книги мультфильмы по ее имени
    def test_get_book_genre_cartoons(self):
        collector = BooksCollector()
        name = 'Смешарики'
        genre = 'Мультфильмы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # Получаем пустой жанр книги по имени книги, у которой не установили жанр
    def test_get_book_genre_without_genre(self):
        collector = BooksCollector()
        name = 'Алгебра'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    # Выводим список книг с жанром комедия
    def test_get_books_with_specific_genre_comedies(self):
        collector = BooksCollector()
        name = 'Дневник Бриджит Джонс'
        genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    # Получаем корректный словарь из добавленных книг
    def test_get_books_genre_correct(self):
        collector = BooksCollector()
        name = 'Дневник Бриджит Джонс'
        genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        expected_result = {name: genre}
        assert collector.get_books_genre() == expected_result

    # Возвращаем книги, подходящие детям, используя корректный жанр
    def test_get_books_for_children_correct_genre(self):
        collector = BooksCollector()
        name = 'Смешарики'
        genre = 'Мультфильмы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == [name]

    # Возвращаем пустой список, используя жанр, не подходящий детям
    def test_get_books_for_children_incorrect_genre(self):
        collector = BooksCollector()
        name = 'Дракула'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == []

    # Добавляем книгу в избранное
    def test_add_book_in_favorites_correct(self):
        collector = BooksCollector()
        name = '1984'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]

    # Удаляем книгу из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        name = '1984'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.get_list_of_favorites_books() == []

    # Получаем список избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        name = '1984'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]
