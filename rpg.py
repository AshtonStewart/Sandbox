"""
Ashton Jack Stewart
Turn based combat style game used to practice inheritance and class handling.
"""

from characters import Characters
from monsters import Monster
from heros import Heroes

PINK_SLIME = Monster("Pink Slime", 200, 10, 20, "goopy")

KNIGHT = Heroes("Knight", 200, 80, 250, "Big punch", "Defend")


def main():
    characters = [PINK_SLIME, KNIGHT]

    HERO = KNIGHT
    MONSTER = PINK_SLIME

    while MONSTER.hp > 0 and HERO.hp > 0:
        player_turn = True
        while player_turn == True:
            print("You are fighting a slime. What do you want to do?")
            print("F to fight. \nD to defend.")
            move = input("What do you do? ")
            if move.upper() == "F":
                attack(HERO, MONSTER)
                player_turn = False
            if move.upper() == "D":
                HERO.defense_raise()
                player_turn = False

        for character in characters:
            if character.hp <= 0:
                print(f"{character.name} is defeated.")

        attack(MONSTER, HERO)


def attack(attacker, defending):
    """Has a monster attack a person"""
    damage = attacker.calc_damage()
    defending.take_damage(damage)

    print(f"{attacker.name} is attacking the {defending.name}.")
    print(f"{defending.name} now has {defending.hp} hp")


main()
