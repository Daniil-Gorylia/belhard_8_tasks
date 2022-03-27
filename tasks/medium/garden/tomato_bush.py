import tomato


class TomatoBush:
    tomato_list: list
    copy_list = []

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        for i in range(len(self.tomato_list)):
            self.tomato_list[i].grow()

    def all_are_ripe(self):
        if all(self.tomato_list[i].is_ripe() for i in range(len(self.tomato_list))):
            return True
        else:
            return False

    def give_away_all(self):
        copy_list = self.tomato_list.copy()
        self.tomato_list.clear()
        return copy_list

if __name__ == '__main__':
    first_tomato = tomato.Tomato(1)
    second_tomato = tomato.Tomato(2)
    third_tomato = tomato.Tomato(3)
    first_tomatoBush = TomatoBush(first_tomato, second_tomato, third_tomato)
    print(first_tomatoBush.tomato_list[0].index)
    print(first_tomatoBush.tomato_list[1].index)
    print(first_tomatoBush.tomato_list[2].index)
    first_tomatoBush.grow_all()
    first_tomatoBush.grow_all()
    print(first_tomatoBush.all_are_ripe())
    first_tomatoBush.grow_all()
    print(first_tomatoBush.all_are_ripe())
    print(first_tomatoBush.give_away_all())
    print(first_tomatoBush.tomato_list)