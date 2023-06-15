# farm
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = True

    def get_older(self):
        self.age += 1

    def speak(self):
        print("... jestem zwierzęciem, które nie umie speak")


class Cow(Animal):
    # Cow nadpisuje metodę speak Animal
    def speak(self):
        print(f"Muuuuuuuuuuuuuuuu, jestem krową o imieniu {self.name}")

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

    def give_milk(self, canka):
        if not self.hungry:
            canka.fill()
            self.hungry = True
        else:
            print("Ej, najpierw może byś mnie nakaremił, co ??")


class Horse(Animal):
    # Horse rozbudowuję metodę speak Animal
    def speak(self):
        super().speak()
        print(f"Ihaaaaaaa, żartowałem. Oczywiście jestem koniem o imieniu {self.name}")


class Hedgehog(Animal):
    # Hedgehog dziedziczy metodę speak Animal
    pass


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


# 4. Dziedziczenie (ang. inheritance)
# Najsilniejszy typ powiązania
# A dziedziczy po B - A "jest" B


# W ramach dziedziczenia mogą zadziać się trzy rzeczy:
# 1. metoda rodzica może zostać oddziedziczona przez dziecko (jeż dziedziczy metodę speak zwierzęcia)
# 2. metoda rodzica może zostać nadpisana przez dziecko (krowa napisuje metodę speak zwierzęcia)
# 3. metoda rodzica może zostać rozbudowana przez dziecko (koń rozbudowuje metodę speak zwierzęcia)
print("===Jeż speak (dziedziczy)===")
h = Hedgehog('jerzy', 5)
h.speak()
print("===Krowa speak (nadpisuje)===")
c.speak()
print("===Koń speak (rozbudowuje)===")
horse = Horse("Caro", 1)
horse.speak()