class Human:
    def __init__(self, name, health, strength, speed):
        self.name = name
        self.health = health
        self.speed = speed
        self.strength = strength

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self , enemy):
        enemy.health -= self.strength
        print(f"[STRIKE] {self.name} throws hands {enemy.name} now has {enemy.health} health")

    
    def counter(self, enemy):
        enemy.health -= self.strength + 30
        print(f"[MY BOI GOT THAT DEFENSE] {enemy.name} took his punch {self.strength + 30} DMG and they now have {enemy.health}")

