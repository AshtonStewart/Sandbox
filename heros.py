"""
Hero class for rpg.py game
"""
from characters import Characters

import random

class Heroes(Characters):
    def __init__(self, name, hp, attack, defense, ability1="", ability2=""):
        super().__init__(name, hp, attack, defense)
        self.ability1 = ability1
        self.ability2 = ability2


    def __str__(self):
        return f"{super().__str__()} and the special abilities {self.ability1} and {self.ability2}!"




