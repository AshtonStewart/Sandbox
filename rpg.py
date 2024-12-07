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
ICE_DRAGON = Monster("Ice Dragon", 2000, 200, 400, "FrostBite")
FIRE_DRAGON = Monster("Fire Dragon", 2000, 300, 200, "Fire breath")

# Heroes
KNIGHT = Heroes("Knight", 300, 80, 250, "Great attack", "Defend")
MAGE = Heroes("Wizard", 100, 200, 50, "Fireball", "Weaken")
SUPPORT = Heroes("Priest", 100, 20, 50, "Heal", "Empower")

ABILITY_DESCRIPTION = "Powerful attacks that (will eventually have a cooldown associated) deal extra damage, either to multiple characters or bestow buffs and debuffs."
HERO_ABILITIES = {"Great attack": "Deals a heavy blow, dealing triple damage but reduces defence",
                  "Defend": "Increases defense by 25%",
                  "Fireball": "A powerful attack that deals medium damage to a group of enemies",
                  "Weaken": "Severely reduce an enemies defense and attack",
                  "Heal": "Resurrect and/ or heal a fallen friend",
                  "Empower": "Increase damage and defense of chosen ally by a bit"}


def main():
    """Gives the options for the player. Currently, the only options are combat, might add some adventure thing later. """
    playable_characters = [KNIGHT, MAGE, SUPPORT]
    monsters = [PINK_SLIME, BLUE_SLIME, GREEN_SLIME]
    #characters = playable_characters + monsters

    health_pools = return_party_health(playable_characters, monsters)

    while health_pools[0] > 0 and health_pools[1] > 0:
        health_pools = return_party_health(playable_characters, monsters)

        for hero in playable_characters:
            if hero.hp > 0:
                player_turn = True
                while player_turn == True:
                    print("F to fight. \n"
                          "S to see stats and abilities\n"
                          "A to use abilities.\n")
                    move = input(f"What will the {hero.name} do? ")

                    if move.upper() == "S":
                        print_characters(playable_characters, monsters)
                        print_abilities()
                    elif move.upper() == "F":
                        attack_monster(hero, monsters)
                        player_turn = False
                    elif move.upper() == "A":
                        use_ability()

        print("\n\nThe monsters are now attacking!")
        have_monsters_attack(monsters, playable_characters)

    if health_pools[0] == 0 and health_pools[1] > 0:
        print("Your party was defeated by the monsters!")
    elif health_pools[1] == 0 and health_pools[0] > 0:
        print("Your party defeated the monsters!")


def attack_monster(hero, monsters):
    """Have the player attack a monster"""
    valid_int = False
    for i, monster in enumerate(monsters):
        print(f"{i + 1}. {monster.name} (HP: {monster.hp})")

    while valid_int == False:

        try:
            valid_selection = False

            while valid_selection == False:
                monster_to_attack = int(input("Please give the number of the monster you want to attack! "))
                monster_to_attack -= 1

                if monster_to_attack in range(0, len(monsters)):
                    if monsters[monster_to_attack].hp <= 0:
                        print("This meant to be a power move or something?")
                    else:
                        attack(hero, monsters[monster_to_attack])
                    valid_int = True
                    valid_selection = True
                else:
                    print("Peace was never an option.")

        except ValueError:
            print("Peace was never an option.")


def attack(attacker, defending):
    """Has a monster attack a person"""
    damage = attacker.calc_damage()
    defending.take_damage(damage)

    print(f"{attacker.name} is attacking the {defending.name}, who now has {defending.hp} HP.")
    if defending.hp <= 0:
        print(f"{defending.name} was defeated")


def return_party_health(playable_characters, monsters):
    """Returns the pary hp to tell if """
    monster_party_hp = sum(monster.hp for monster in monsters)
    playable_party_hp = sum(character.hp for character in playable_characters)

    return monster_party_hp, playable_party_hp


def have_monsters_attack(monsters, playable_characters):
    """Let each monster attack a party member"""
    target = None

    for monster in monsters:
        if monster.hp > 0:
            valid_target = False

            while valid_target == False:
                if random.randint(0, 15) != 15:
                    target_index = random.randint(0, len(playable_characters) - 1)
                    target = playable_characters[target_index]
                    if target.hp > 0:
                        valid_target = True
                else:
                    target_index = random.randint(0, len(monsters) - 1)
                    target = monsters[target_index]
                    if target.hp > 0:
                        valid_target = True
                        print(f"{monster.name} has gotten confused and is now attacking the {target.name}!?")

                # Add a secret in here saying they can attack themselves?

                attack(monster, target)


def print_abilities():
    """Prints the dictionary of abilities and what they do."""

    print("\n\nAbilities:")
    for abilities in HERO_ABILITIES:
        print(f"{abilities:10}: {HERO_ABILITIES[abilities]}")
    print("(Abilities are not exclusive to monsters or Heroes and monsters)")


def print_characters(playable_characters, monsters):
    """Prints the stats of eveybody in the fight"""

    print("Heroes: ")
    for playable in playable_characters:
        print(playable)

    print("Monsters: ")
    for monster in monsters:
        print(monster)


def use_ability():
    print("")


main()
