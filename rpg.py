"""
Ashton Jack Stewart
Turn based combat style game used to practice inheritance and class handling.
"""

from characters import Characters
from monsters import Monster
from heros import Heroes

Slime = Monster("slime", 100, 10, 20, "goopy")

knight = Heroes("Knight", 200, 100, 250, "Big punch")


def main():
    while Slime.hp > 0 and knight.hp > 0:
        player_turn = True
        while player_turn == True:
            print("You are fighting a slime. What do you want to do?")
            move = input("F for fight. ")
            if move.upper() == "F":
                # attacker = input("Choose the character to attack: ").lower()
                # defending = input("Choose who they're attacking: ").lower()

                attacker = knight
                defending = "slime"
                attack(attacker, defending)
        # function enemy_attack


def attack(attacker, defending):
    """Has a monster attack a person"""
    print(f"{attacker.name} is attacking the {defending}.")
    damage = attacker.calc_damage()
    print(damage)


main()
