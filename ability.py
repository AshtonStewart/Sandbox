"""
Class for each ability to keep track of stats and such
"""

class Ability:

    def __init__(self, name="", cooldown = 0, splash = False, target = ""):
        """Constructor for Ability class"""
        self.name = name
        self.cooldown = cooldown
        self.recharge = cooldown #cooldown acts as a constant while recharge changes so it's know if it's available or not
        self.splash = splash
        self.target = target

    def start_battle(self):
        self.recharge = self.cooldown

    def calc_recharge(self):
        if self.recharge < self.cooldown:
            self.recharge += 1

    def use_ability(self):
        self.recharge = 0

    def is_available(self):
        if self.recharge == self.cooldown:
            return "(Avialable)", True
        else:
            return f"(On cooldown. Available in {self.cooldown - self.recharge} turns)", False
