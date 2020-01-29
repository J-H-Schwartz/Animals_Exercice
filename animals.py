class AgeInvalide(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = tuple([arg])
        try:
            raise AgeInvalide("L'age est invalide !")
        except AgeInvalide as e:
            print("Age Invalide Exception !", e.strerror)


class Animals:
    _diet = []
    cri = ""
    weight = 0
    life_esperance = 0
    _age = 0

    def __init__(self, name, age, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
        self.age = age

    def get_age(self):
        return self._age

    def set_age(self, value):
        if 0 < value < self.life_esperance:
            self._age = value
        else:
            raise AgeInvalide(value)

    age = property(get_age, set_age)

    def talk(self):
        return self.cri

    def eat(self, aliment, name):
        diet = self._diet
        if aliment in diet:
            print("{} mange {}. Son poids augmente de 5%".format(name, aliment))
            self.weight += (self.weight * 5) / 100
            return True
        else:
            print("L'aliment {} ne fait pas partie du régime de {}.".format(aliment, name))
            return False


class MutedAnimals:

    def talk(self):
        return "Cet animal ne parle pas."


class Cat(Animals):
    _diet = ["viande", "poisson"]
    cri = "Miaou"
    hair_type = "hair"
    life_esperance = 12


class Snake(Animals):
    _diet = ["viande", "rongeur", "insecte"]
    cri = "SSSsss"
    hair_type = "tiles"
    life_esperance = 6


class Snail(MutedAnimals, Animals):
    _diet = ["plante", "salade", "insecte"]
    cri = "???"
    hair_type = "tiles"
    life_esperance = 1


cat = Cat("Felix", 5, 1.5, "black")
print(cat.talk())
print(cat.age)
print(cat.weight)
cat.eat("poisson", cat.name)
print(cat.weight)

snake = Snake("Bob", 2, 6, "green and yellow")
print(snake.talk())
print(snake.age)
print(snake.weight)
snake.eat("poisson", snake.name)
print(snake.weight)

snail = Snail("Jojo", 0.1, 0.01, "green")
print(snail.talk())
print(snail.age)
print(snail.weight)
snail.eat("plante", snail.name)
print(snail.weight)
