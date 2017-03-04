from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# create black magic
fire = Spell('Fire', 10, 100, 'BlackMagic')
meteor = Spell('Metoer', 15, 150, 'BlackMagic')
earthquake = Spell('Earthquake', 10, 100, 'BlackMagic')
thunderShock = Spell('ThunderShock', 8, 80, 'BlackMagic')
bolt = Spell('Bolt', 5, 50, 'BlackMagic')
void = Spell('void', 20, 200, 'BlackMagic')

# create white magic
cure = Spell('Cure', 10, 80, 'whiteMagic')
cura = Spell('Cura', 20, 200, 'whiteMagic')

# create some items, for healing purpose
potion = Item('Potion', 'potion', 'heals for 50HP', 50, 10)
SuperPotion = Item('SuperPotion', 'potion', 'heals for 250HP', 250, 5)
Elixer = Item('Elixer', 'elixer', 'restores max hp/mp of one party member', 9999, 5)
PartyElixer = Item('PartyElixer', 'PartyElixer', 'restores all party members hp/mp to max', 9999, 2)

# create some items for damage purpose
grenade = Item('grenade', 'attack', 'deals 500 damage', 500, 3)

promptStory = str(input("\nThis is a Game between good and evil. You control the army of Superhero's.\nYour Generals "
                        "are MintBerry, Mysterion, and the HumanKite.\nYou face the evil army led by The_Coon, "
                        "with his minions Professor Chaos and General DisArray.\nAre You Up For The Challenge?\n"))

player_items = [potion, SuperPotion, Elixer, PartyElixer, grenade]
player_spells = [fire, meteor, earthquake, thunderShock, bolt, void, cure, cura]

# players team
player1 = Person(800, 60, 60, 35, player_spells, player_items, 'MintBerry')
player2 = Person(800, 100, 60, 60, player_spells, player_items, 'Mysterion')
player3 = Person(800, 60, 60, 35, player_spells, player_items, 'HumanKite')
players = [player1, player2, player3]

# Enemies
enemy1 = Person(1500, 45, 100, 25, player_spells, player_items, 'The_Coon')
enemy2 = Person(700, 45, 100, 25, player_spells, player_items, 'ProfChaos')
enemy3 = Person(500, 45, 100, 25, player_spells, player_items, 'DisArray')
enemies = [enemy1, enemy2, enemy3]

cond = True
i = 0


# a function testing to see if the game is over
def is_it_over():
    global cond
    global player1
    global player2
    global player3
    global enemy1
    global enemy2
    global enemy3
    if enemy1.get_hp() == 0 and enemy2.get_hp() == 0 and enemy3.get_hp() == 0:
        print(Bcolors.OKGREEN + Bcolors.BOLD + '\n' + 'YOU WIN!' + Bcolors.ENDC)
        cond = False
    elif player1.get_hp() == 0 and player2.get_hp() == 0 and player3.get_hp() == 0:
        print(Bcolors.FAIL + Bcolors.BOLD + '\n' + "YOU LOOSE!" + Bcolors.ENDC)
        cond = False


print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)


def score_board():
    for player in players:
        player.get_score_board()

    print(Bcolors.FAIL + Bcolors.BOLD + '\nENEMY' + Bcolors.ENDC)
    for enemy in enemies:
        enemy.get_enemy_score_board()


while cond:
    print('\n=======================')
    print('\n')
    score_board()
    for player in players:

        if player.get_hp() == 0:
            continue

        print('=======================')
        print('\n')
        print(player.get_name())
        player.choose_action()
        choice = input('\nChoose action:')
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            player.choose_target(enemies)
            enemy_target = int(input('\nChoose your target:')) - 1
            enemies[enemy_target].take_damage(dmg)
            print(Bcolors.OKBLUE + player.get_name() + ' attacked for ' + str(dmg) + ' points of damage.' + enemies[
                enemy_target].get_name() + ' Hp is ' + str(enemies[enemy_target].get_hp()) + Bcolors.ENDC)
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input('\nChoose which spell:')) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(Bcolors.FAIL + '\nNot enough magic points!' + Bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.thisType == 'whiteMagic':
                player.heal(magic_dmg)
                print(Bcolors.OKBLUE + '\n' + spell.name + ' heals for ' + str(magic_dmg) + 'HP. Your HP is now ' + str(
                    player.get_hp()) + Bcolors.ENDC)
            elif spell.thisType == 'BlackMagic':
                player.choose_target(enemies)
                enemy_target = int(input('\nChoose your target:')) - 1
                enemies[enemy_target].take_damage(magic_dmg)
                print(Bcolors.OKBLUE + '\n' + spell.name + ' deals ', str(magic_dmg),
                      'points of damage.' + enemies[enemy_target].get_name() + ' hp is ',
                      str(enemies[enemy_target].get_hp()) + Bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input('\nChoose Item: ')) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]

            if item.quantity == 0:
                print('=======================')
                print(
                    Bcolors.FAIL + '\n' + player.name + ', you do not have any ' + item.name + ' left to use!'
                    + Bcolors.ENDC)
                continue

            player.reduce_item_quantity(item_choice)

            if item.thisType == 'potion':
                player.heal(item.prop)
                print(Bcolors.OKBLUE + '\n' + item.name + ' heals for ' + str(item.prop) + ' HP' + Bcolors.ENDC)
            elif item.thisType == 'elixer':
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(Bcolors.OKBLUE + '\n' + item.name + ' fully restores both HP and MP!' + Bcolors.ENDC)
            elif item.thisType == 'PartyElixer':
                for person in players:
                    person.hp = person.maxhp
                    person.mp = person.maxmp
                print(
                    Bcolors.OKBLUE + '\n' + item.name + ' fully restores both HP and MP of all party members!'
                    + Bcolors.ENDC)
            elif item.thisType == 'attack':
                player.choose_target(enemies)
                enemy_target = int(input('\nChoose your target:')) - 1
                enemies[enemy_target].take_damage(item.prop)
                print(Bcolors.OKBLUE + '\n' + player.name + ' used a ' + item.name + ' and dealt ' + str(
                    item.prop) + ' points of damage!' + Bcolors.ENDC)

        score_board()
        is_it_over()
        if cond == False:
            break

    for enemy in enemies:
        if enemy.get_hp() == 0:
            continue
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            enemy_dmg = enemy.generate_damage()
            target = random.randrange(0, 3)
            players[target].take_damage(enemy_dmg)
            print('\n=======================\n' + Bcolors.FAIL + Bcolors.BOLD + enemy.name + ' attacked ' + players[
                target].name + ' for ' + str(enemy_dmg), 'points of damage. ' + players[target].name + ' Hp is ' + str(
                players[target].get_hp()) + Bcolors.ENDC)

        elif enemy_choice == 1:
            enemy_spell = random.randrange(0, 8)
            spell = enemy.magic[enemy_spell]
            enemy_mp = enemy.get_mp()
            magic_dmg = spell.generate_damage()

            if spell.cost > enemy_mp:
                continue

            enemy.reduce_mp(spell.cost)

            if spell.thisType == 'whiteMagic':
                enemy.heal(magic_dmg)
                print('\n=======================\n' + Bcolors.FAIL + Bcolors.BOLD + spell.name + ' heals for ' + str(
                    magic_dmg) + 'HP. ' + enemy.name + ' HP is now ' + str(enemy.get_hp()) + Bcolors.ENDC)
            if spell.thisType == 'BlackMagic':
                spell_target = random.randrange(0, 3)
                players[spell_target].take_damage(magic_dmg)
                print('\n=======================\n' + Bcolors.FAIL + Bcolors.BOLD + spell.name + ' deals ',
                      str(magic_dmg), 'points of damage.' + players[spell_target].name + ' hp is ',
                      str(players[spell_target].get_hp()) + Bcolors.ENDC)

        is_it_over()
        if cond == False:
            break
