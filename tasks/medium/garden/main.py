import gardener
import tomato
import tomato_bush

if __name__ == '__main__':
    first_tomato = tomato.Tomato(1)
    second_tomato = tomato.Tomato(2)
    third_tomato = tomato.Tomato(3)
    fourth_tomato = tomato.Tomato(4)
    fifth_tomato = tomato.Tomato(5)
    first_tomatoBush = tomato_bush.TomatoBush(first_tomato, second_tomato, third_tomato)
    second_tomatoBush = tomato_bush.TomatoBush(fourth_tomato, fifth_tomato)
    first_gard = gardener.Gardener('Peter', first_tomatoBush, second_tomatoBush)
    first_gard.work()
    first_gard.work()
    print(first_gard.harvest())
    first_gard.work()
    print(first_gard.harvest())
    print(first_tomatoBush.tomato_list)
    print(second_tomatoBush.tomato_list)
