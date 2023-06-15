# 2. Agregajca
# Silniejsze sprzężenie dwóch klas (tzw. agreagacja ang. aggreagation)
# A agreguje B - A "składa się z i nie odpowiada za tworzenie" B (nie odpowiada za inicjalizację B)
class Computer:
    def __init__(self, component):
        self.component = component


class Component:
    def __init__(self, name):
        self.name = name


c = Component("CPU")  # komponent c powstał poza komputerem
comp = Computer(c)  # i został przekazany do komputera w inicjalizatorze (to jest defnicja agregacji)


# 3. Kompozycja
# Jeszcze silniejsz sprzężenie dwóch klas to kompozycja tzw. composition
# A komponuje się z B - A "składa się i odpowiada za tworzenie" B
class Computer:
    def __init__(self, comp_name):
        self.component = Component(comp_name)


class Component:
    def __init__(self, name):
        self.name = name


comp = Computer("CPU")  # do inicjalizotora klasy przekazywany jest tylko string
# a w inicjlizatorze klasy Computer tworzony jest obiekt klasy Component. Klasa Computer odpowiada za stworzenie
# obiektu klasy component