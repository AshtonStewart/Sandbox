"""
Hero class for rpg.py game
"""
from characters import Characters

import random

class Heroes(Characters):
    def __init__(self, name, hp, attack, defense, ability):
        super().__init__(name, hp, attack, defense)
        self.ability = ability

    def __str__(self):
        return f"{super().__str__()} and the special ability {self.ability}!"


    def calc_damage(self):
        attack_multi = random.randint(0, 50) / 100
        damage = self.attack
        attack_diff = random.randint(0, 4)
        if attack_diff != 4:
            if random.randint(0, 1) == 1:
                damage += (damage * attack_multi)
            else:
                damage -= (damage * attack_multi)
            return f"{self.name} has dealt {damage} damage!"
        else:
            damage = self.attack * 2
            return f"{self.name} has a critical hit worth {damage} damage!"

