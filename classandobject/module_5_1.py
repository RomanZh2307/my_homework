class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(int(new_floor)):
            if int(new_floor) > self.number_of_floors or self.number_of_floors < 1:
                print("Такого этажа не существует")
                break

            else:
                print(i + 1)
                i = + 1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
