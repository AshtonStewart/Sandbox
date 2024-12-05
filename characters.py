""""""

import random

class Characters:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} has {self.hp} hp, {self.attack} attack power and {self.defense} defense"

