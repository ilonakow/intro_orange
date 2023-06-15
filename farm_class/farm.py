# farm
class Cow:
    # inicjalizator (metoda magiczna)
    def __init__(self, name, age):
        """To tutaj grupuje się wszystkie cechy (atrybuty) klasy"""
        # zestaw wszystkich atrybutów nazywany jest stanem obiektu
        self.name = name
        self.age = age
        self.hungry = True

    # metoda czytająca stan obiektu (atrubut name)
    def speak(self):
        print(f"Muuuuuuuuuuuuuuuu, jestem krowa o imieniu {self.name}")
        print(f"Muuuuuuuuuuuuuuuu, jestem krową o imieniu {self.name}")

    # metody modyfikujące stan obiektu
    def eat(self, meal):
        if self.hungry:
            if meal == 3:
                print('To nie wiesz, że 3 się nie je, debilu!')
            else:
                print(f"Jem {meal}")
                self.hungry = False
        else:
            print("Ha, nie jestem głodna. I co mi zrobisz?")
    def run(self):
        print("Biegam, biegam, biegam ...")
        self.hungry = True
        print("aż zgłodniałam")
    def get_older(self):
        self.age += 1
    def give_milk(self, canka):
        if not self.hungry:
            canka.fill()
            self.hungry = True
        else:
            print("Ej, najpierw może byś mnie nakaremił, co ??")
class Canka:
    def __init__(self, volume):
        self.volume = volume
        self.is_full = False
    def fill(self):
        self.is_full = True
c = Cow("Mućka", 2)
c.speak()
c.eat("trawa")
c.eat("woda")
c.run()
c.eat("woda")
print(f"Krowa {c.name} ma {c.age} lat.")
c.get_older()
print(f"Krowa {c.name} ma {c.age} lat.")

# 1. Zależność
# Powiązujemy (sprzęgamy, ang. coupling) ze sobą dwa obiekty w najsłabszy możliwy sposób (tzw. zależność, ang. dependency)
# Zależność A od B oznacz - A "korzysta z / używa" B
k = Canka(5)
c.give_milk(k)
#
# class Goat:
#
#     def __init__(self, name, age, new_name):
#         self.group = "domowa"
#         self.name = name
#         self.age = age
#         self.new_name = new_name
#     def eat(self):
#         print("mniam")
#
#     def change_name(self):
#         print("zmieniam imie")
#
#
# g = Goat("Matołek", 4, "Puszek")
# g.eat()
#
# print(f"To jest koza {g.group}, ma {g.age} lata, nazywa się {g.name}. Zmieniłam imię na {g.new_name}")