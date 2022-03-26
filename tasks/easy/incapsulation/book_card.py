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
        self.author = author
        self.title = title
        self.year = year

    def sorting_book(self):
        pass

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @author.setter
    def author(self, a):
        if not isinstance(a, str):
            raise ValueError
        else:
            self.__author = a

    @title.setter
    def title(self, t):
        if not isinstance(t, str):
            raise ValueError
        else:
            self.__title = t

    @year.setter
    def year(self, y):
        if not isinstance(y, int):
            raise ValueError
        elif not y > 0:
            raise ValueError
        elif y > CURRENT_YEAR:
            raise ValueError
        else:
            self.__year = y
