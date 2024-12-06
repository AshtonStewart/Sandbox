"""
Ashton Jack Stewart
Turn based combat style game used to practice inheritance and class handling.
"""

from characters import Characters
from monsters import Monster
from heros import Heroes
import random

# Enemies
PINK_SLIME = Monster("Pink Slime", 200, 10, 20, "Goopy")
BLUE_SLIME = Monster("Blue Slime", 500, 20, 40, "More Goopy")
GREEN_SLIME = Monster("Green Slime", 1000, 50, 60, "Goopiest!")

# Heroes
KNIGHT = Heroes("Knight", 200, 500, 250, "Big punch", "Defend")
MAGE = Heroes("Wizard", 100, 200, 100, "Fireball", "Weaken")


def main():
    """Gives the options for the player. Currently, the only options are combat, might add some adventure thing later. """
    playable_characters = [KNIGHT, MAGE]
    monsters = [PINK_SLIME, BLUE_SLIME, GREEN_SLIME]
    characters = playable_characters + monsters

    MONSTER = GREEN_SLIME

    health_pools = return_party_health(playable_characters, monsters)

    # monster_party_hp = sum(monster.hp for monster in monsters)
    # playable_party_hp = sum(character.hp for character in playable_characters)

    while health_pools[0] > 0 and health_pools[1] > 0:
        health_pools = return_party_health(playable_characters, monsters)

        for hero in playable_characters:
            player_turn = True

            while player_turn == True:
                print("F to fight. \n"
                      "S to see stats\n")
                move = input(f"What will the {hero.name} do? ")

                if move.upper() == "S":
                    for character in characters:
                        print(character)
                elif move.upper() == "F":
                    attack(hero, MONSTER)
                    player_turn = False

        print("\n\nThe monsters are now attacking!")
        have_monsters_attack(monsters, playable_characters)

        for character in characters:
            if character.hp <= 0:
                print(f"{character.name} is defeated.")

    if health_pools[0] == 0:
        print("Your party was defeated by the monsters!")
    elif health_pools[1] == 0:
        print("Your party defeated the monsters!")


def attack(attacker, defending):
    """Has a monster attack a person"""
    damage = attacker.calc_damage()
    defending.take_damage(damage)

    print(f"{attacker.name} is attacking the {defending.name}, who now has {defending.hp} HP.")


def return_party_health(playable_characters, monsters):
    """Returns the pary hp to tell if """
    monster_party_hp = sum(monster.hp for monster in monsters)
    playable_party_hp = sum(character.hp for character in playable_characters)

    return monster_party_hp, playable_party_hp


def have_monsters_attack(monsters, playable_characters):
    """Lets each monster attack a party member"""

    for monster in monsters:
        valid_target = False
        while valid_target == False:
            target_index = random.randint(0, len(playable_characters) - 1)
            target = playable_characters[target_index]
            if target.hp > 0:
                valid_target = True
        if monster.hp > 0:
            attack(monster, target)


main()
