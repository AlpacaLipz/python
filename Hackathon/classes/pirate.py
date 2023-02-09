from classes.human import Human
class Pirate(Human):
    def __init__(self, Pirate_name):
        super().__init__(Pirate_name, 100, 15, 3)

    def counter(self, enemy):
        enemy.health -= self.strength + 10
        print(f"[MY BOI GOT THAT DEFENSE] {enemy.name} took his punch {self.strength + 10} DMG and they now have {enemy.health}")




