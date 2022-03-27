class Tomato:
    index: int
    ripeness: str
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index, ripeness=states[0]):
        self.index = index
        self.ripeness = ripeness

    def grow(self, states=states):
        for i in range(len(states)):
            if states[i] == self.ripeness:
                if self.ripeness != states[len(states) - 1]:
                    self.ripeness = states[i + 1]
                    break
                else:
                    break

    def is_ripe(self, states=states):
        if self.ripeness == states[len(states) - 1]:
            return True
        else:
            return False


if __name__ == '__main__':
    first_tomato = Tomato(1)
    print(type(first_tomato.states))
    print(first_tomato.states[len(first_tomato.states) - 1])
    print(list(range(len(first_tomato.states))))
    print(f"start {first_tomato.ripeness}")
    first_tomato.grow()
    print(f"next1 {first_tomato.ripeness}")
    first_tomato.grow()
    print(f"next2 {first_tomato.ripeness}")
    if first_tomato.is_ripe():
        print("уже созрел")
    else:
        print("еще не созрел")
    first_tomato.grow()
    print(f"next3 {first_tomato.ripeness}")
    if first_tomato.is_ripe():
        print("уже созрел")
    else:
        print("еще не созрел")
    first_tomato.grow()
    print(f"next4 {first_tomato.ripeness}")
