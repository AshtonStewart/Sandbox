""""""

import random
import math

class Characters:
    def __init__(self, name="", hp=0.0, attack=0.0, defense=0.0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} has {self.hp} hp, {self.attack} attack power and {self.defense} defense"

    def take_damage(self, taken_damage):
        defense_buff = random.randint(1, 50) / 100
        defense_buff *= self.defense

        if defense_buff >= taken_damage/2:
            taken_damage = taken_damage/2
        else:
            taken_damage -= defense_buff


        if taken_damage >= self.hp:
            self.hp = 0
        else:
            self.hp -= taken_damage
            self.hp = math.ceil(self.hp)

    def calc_damage(self):
        attack_multi = random.randint(0, 50) / 100
        damage = self.attack
        attack_diff = random.randint(0, 4)
        if attack_diff != 4: #regular attack variance
            if random.randint(0, 1) == 1:
                damage += (damage * attack_multi)
            else:
                damage -= (damage * attack_multi)

        else: #Critical hit
            damage = self.attack * 2

        return damage

    def defense_raise(self):
        self.defense += (self.defense * 1.5)