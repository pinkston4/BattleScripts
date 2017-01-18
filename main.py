from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item

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

#create some items, for healing purpose
potion = Item('Potion', 'potion', 'heals for 50HP', 50, 5)
SuperPotion = Item('SuperPotion', 'potion', 'heals for 250HP', 250, 2)
Elixer = Item('Elixer', 'elixer', 'restores max hp/mp of one party member', 9999, 2)
PartyElixer = Item('PartyElixer', 'elixer', 'restores all party members hp/mp to max', 9999, 1)

#create some items for damage purpose
grenade = Item('grenade', 'attack', 'deals 500 damage', 500, 2)

name = str(input('\nWhat should we call you?\n==='))


player_items = [potion, SuperPotion, Elixer, PartyElixer, grenade]
player_spells = [fire, meteor, earthquake, thunderShock, bolt, void, cure, cura]

#players team
player1 = Person(800, 60, 60, 35, player_spells, player_items, name)
player2 = Person(800, 60, 60, 60, player_spells, player_items, 'Kenny')
player3 = Person(800, 60, 60, 35, player_spells, player_items, 'Stan')

players = [player1, player2, player3]
#Enemies
enemy = Person(1200, 45, 80, 25, [], [])

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
	print('=======================')
	
	for player in players:
		player.get_score_board()

	print('\n')
	for player in players:
		player.choose_action()
		choice = input('\nChoose action:')
		index = int(choice) - 1

		if index == 0:
			dmg = player.generate_damage()
			enemy.take_damage(dmg)
			print(Bcolors.OKBLUE + player.name + ' attacked for ' + str(dmg) + ' points of damage.' + enemy.name + ' Hp is ' + str(enemy.get_hp()) + Bcolors.ENDC)
		elif index == 1:
			player.choose_magic()
			magic_choice = int(input('\nChoose which spell:')) -1

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
				print(Bcolors.OKBLUE + '\n' + spell.name + ' heals for ' + str(magic_dmg) + 'HP. Your HP is now ' + str(player.get_hp()) + Bcolors.ENDC)
			elif spell.thisType == 'BlackMagic':
				enemy.take_damage(magic_dmg)
				print(Bcolors.OKBLUE + '\n' + spell.name + ' deals ', str(magic_dmg), 'points of damage.' + enemy.name + ' hp is ', str(enemy.get_hp()) + Bcolors.ENDC)

		elif index == 2:
			player.choose_item()
			item_choice = int(input('\nChoose Item: ')) -1

			if item_choice == -1:
				continue

			item = player.items[item_choice]

			if item.quantity == 0:
				print('=======================')
				print(Bcolors.FAIL + '\n' + player.name + ', you do not have any ' + item.name + ' left to use!' + Bcolors.ENDC)
				continue

			item.quantity -= 1

			if item.thisType == 'potion':
				player.heal(item.prop)
				print(Bcolors.OKBLUE + '\n' + item.name + ' heals for ' + str(item.prop) + ' HP' + Bcolors.ENDC)
			elif item.thisType == 'elixer':
				player.hp = player.maxhp
				player.mp = player.maxmp
				print(Bcolors.OKBLUE + '\n' + item.name + ' fully restores both HP and MP!' + Bcolors.ENDC)
			elif item.thisType == 'attack':
				enemy.take_damage(item.prop)
				print(Bcolors.OKBLUE + '\n' + player.name + ' used a ' + item.name + ' and dealt ' + str(item.prop) + ' points of damage!' + Bcolors.ENDC)

		enemy_choice = 1

		enemy_dmg = enemy.generate_damage()
		player.take_damage(enemy_dmg)
		print(Bcolors.FAIL + Bcolors.BOLD + enemy.name + ' attacked ' + player.name + ' for ' + str(enemy_dmg), 'points of damage. ' + player.name + ' Hp is ' + str(player.get_hp()) + Bcolors.ENDC)

		print('=======================')
		print(enemy.name + ' HP: ', Bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + Bcolors.ENDC + '\n')

		print(player.name + ' HP: ', Bcolors.OKGREEN + str(player.get_hp()) + '/' + str(player.get_max_hp()) + Bcolors.ENDC)
		print(player.name + ' MP: ', Bcolors.OKGREEN + str(player.get_mp()) + '/' + str(player.get_max_mp()) + Bcolors.ENDC)

		if enemy.get_hp() == 0:
			print(Bcolors.OKGREEN + Bcolors.BOLD + '\n' + 'YOU WIN!' + Bcolors.ENDC)
			running = False
		elif player.get_hp() == 0:
			print(Bcolors.FAIL + Bcolors.BOLD +  '\n' + "YOU LOOSE!" + Bcolors.ENDC)
			running = False

