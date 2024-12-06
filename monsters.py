"""
Hero class for rpg.py game
"""

from characters import Characters

class Monster(Characters):
    def __init__(self, name, hp, attack, defense, ability=""):
        super().__init__(name, hp, attack, defense)
        self.ability = ability

    def __str__(self):
        return f"{super().__str__()} and the special ability: {self.ability}!"

