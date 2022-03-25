"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, author, title, year):
        self.__author = author
        self.__title = title
        self.__year = year

    def sorting_book(self):
        pass

    @property
    def get_author(self):
        return self.__author

    @property
    def get_title(self):
        return self.__title

    @property
    def get_year(self):
        return self.__year

    @get_author.setter
    def get_author(self, new_author):
        if not isinstance(new_author, str):
            raise ValueError
        else:
            self.__author = new_author

    @get_title.setter
    def get_title(self, new_title):
        if not isinstance(new_title, str):
            raise ValueError
        else:
            self.__title = new_title

    @get_year.setter
    def get_year(self, new_year):
        if not isinstance(new_year, int):
            raise ValueError
        else:
            self.__year = new_year
