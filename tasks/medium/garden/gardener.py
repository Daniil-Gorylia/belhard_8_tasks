import tomato
import tomato_bush


class Gardener:
    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = list(args)     # или arg[0] если передается общим списком после name    (name, (.....,,,,))

    def work(self):
        for i in range(len(self.plants)):
            self.plants[i].grow_all()

    def harvest(self):
        copy_list = []
        if all(self.plants[i].all_are_ripe() for i in range(len(self.plants))):
            for item in self.plants:
                copy_list.append(item.give_away_all())
            return sum(copy_list, [])                      # из списка списков делает список
        else:
            print("Не все томаты созрели.")
            return None


if __name__ == '__main__':
    first_tomato = tomato.Tomato(1)
    second_tomato = tomato.Tomato(2)
    third_tomato = tomato.Tomato(3)
    fourth_tomato = tomato.Tomato(4)
    fifth_tomato = tomato.Tomato(5)
    first_tomatoBush = tomato_bush.TomatoBush(first_tomato, second_tomato, third_tomato)
    second_tomatoBush = tomato_bush.TomatoBush(fourth_tomato, fifth_tomato)
    first_gard = Gardener('Peter', first_tomatoBush, second_tomatoBush)
    first_gard.work()
    first_gard.work()
    print(first_gard.harvest())
    first_gard.work()
    print(first_gard.harvest())
    print(first_tomatoBush.tomato_list)
    print(second_tomatoBush.tomato_list)
