"""
Ashton Jack Stewart
Turn based combat style game used to practice inheritance and class handling.
"""

from characters import Characters
from monsters import Monster
from heros import Heroes
from ability import Ability
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
NECROMANCER = Heroes("Necromancer", 175, 120, 40, "Mortalize", "Resurrect")

ABILITY_DESCRIPTION = "Powerful attacks that (will eventually have a cooldown associated) deal extra damage, either to multiple characters or bestow buffs and debuffs."
HERO_ABILITIES = {"Great attack": "Deals a heavy blow, dealing triple damage but reduces defence",
                  "Defend": "Increases defense by 50% and focuses enemy attacks, at the cost of losing almost all attack power",
                  "Fireball": "A powerful attack that deals medium damage to a group of enemies",
                  "Weaken": "Severely reduce an enemies defense and attack",
                  "Heal": "Resurrect and/ or heal a fallen friend. Resurrecting them will reduce attack. ",
                  "Empower": "Increase damage and defense of chosen ally by a bit",
                  "Resurrect": "Resurrect a friend with equal damage, but low defense and full attack and damage",
                  "Mortalize": "Takes most of the chosen heroes defence and turns it into attack power for themself and the chosen hero."}

# ability = ["Name", cooldown, splash_effect, target]
GREAT_ATTACK = Ability("Great attack", 3, False, "monsters")
FIREBALL = Ability("Fireball", 5, True, "monsters")
DEFEND = Ability("Defend", 8, False, "")

ALL_ABILITIES = [GREAT_ATTACK, DEFEND, FIREBALL]


def main():
    """Gives the options for the player. Currently, the only options are combat, might add some adventure thing later. """
    playable_characters = [KNIGHT, MAGE, SUPPORT]
    monsters = [PINK_SLIME, BLUE_SLIME, GREEN_SLIME]
    # characters = playable_characters + monsters

    health_pools = return_party_health(playable_characters, monsters)
    for abilities in ALL_ABILITIES:
        abilities.start_battle()

    while health_pools[0] > 0 and health_pools[1] > 0:
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
                        choose_ability(hero)
                        player_turn = False
        for abilities in ALL_ABILITIES:
            abilities.calc_recharge()

        # Determines if there's still any enemies left to attack. If so, they attack
        health_pools = return_party_health(playable_characters, monsters)
        if health_pools[1] > 0:
            print("\n\nThe monsters are now attacking!")
            have_monsters_attack(monsters, playable_characters)
        health_pools = return_party_health(playable_characters, monsters)

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
                        attack_character(hero, monsters[monster_to_attack])
                    valid_int = True
                    valid_selection = True
                else:
                    print("Peace was never an option.")

        except ValueError:
            print("Peace was never an option.")


def attack_character(attacker, defending):
    """Has a monster attack a person"""
    damage = attacker.calc_damage()
    defending.take_damage(damage)

    print(f"{attacker.name} is attacking the {defending.name}, who now has {defending.hp} HP.")
    if defending.hp <= 0:
        print(f"{defending.name} was defeated.\n")


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

                attack_character(monster, target)
    print("The monsters are done attacking!")


def print_abilities():
    """Prints the dictionary of abilities and what they do."""
    print("\n\nAbilities:")
    for abilities in HERO_ABILITIES:
        print(f"{abilities:10}: {HERO_ABILITIES[abilities]}")

def print_characters(playable_characters, monsters):
    """Prints the stats of eveybody in the fight"""

    print("Heroes: ")
    for playable in playable_characters:
        print(playable)

    print("Monsters: ")
    for monster in monsters:
        print(monster)


def choose_ability(hero):
    print("Choose the ability to use. \n")
    not_chosen = True
    chosen_ability = None

    check1, check2 = check_hero_ability_availability(hero)

    while not_chosen:
        print(f"1. {hero.ability1} {check1[0]} \n"
              f"2. {hero.ability2} {check2[0]}")
        print("other inputs will display the menu again.\n")
        choice = input("Please choose: ")
        if choice == "1":
            if check1[1]:
                not_chosen = False
                chosen_ability = hero.ability1
            else:
                print("Ability still on cooldown")

        elif choice == "2":
            if check2[1]:
                not_chosen = False
                chosen_ability = hero.ability2
            else:
                print("Ability still on cooldown")
        else:
            print_abilities()

    initiate_ability_affects(hero, chosen_ability)


def check_hero_ability_availability(hero):
    """Check what abilities the hero can use"""
    check1 = ""
    check2 = ""
    for ability in ALL_ABILITIES:
        if ability.name == hero.ability1:
            check1 = ability.is_available()
        if ability.name == hero.ability2:
            check2 = ability.is_available()

    return check1, check2


def initiate_ability_affects(hero, chosen_ability):
    """Gets the information about the ability then proceeds as necessary"""
    #print(chosen_ability)
    abilities = ""
    for abilities in ALL_ABILITIES:
        if chosen_ability == abilities.name:
            print(f"{hero.name} used the ability {chosen_ability}")
            chosen_ability = abilities
            chosen_ability.use_ability()



main()
