from classes.game import Person, Bcolors
from classes.magic import Spell

# create black magic
fire = Spell('Fire', 10, 100, 'BlackMagic')
meteor = Spell('metoer', 15, 150, 'BlackMagic')
earthquake = Spell('earthquake', 10, 100, 'BlackMagic')
thunderShock = Spell('thunderShock', 8, 80, 'BlackMagic')
bolt = Spell('Bolt', 5, 50, 'BlackMagic')
void = Spell('void', 20, 200, 'BlackMagic')

# create white magic
cure = Spell('cure', 10, 80, 'whiteMagic')
charm = Spell('Charm', 10, 100, 'whiteMagic')
cura = Spell('Cura', 20, 200, 'whiteMagic')


player = Person(500, 65, 60, 35, [fire, meteor, earthquake, thunderShock, bolt, void, cure, cura, charm])
enemy = Person(825, 65, 40, 25, [])

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
	print('==================')
	player.choose_action()
	choice = input('Choose action:')
	index = int(choice) - 1

	if index == 0:
		dmg = player.generate_damage()
		enemy.take_damage(dmg)
		print(Bcolors.OKBLUE + 'You attacked for' + str(dmg) + ' points of damage. Enemy Hp is ' + str(enemy.get_hp()) + Bcolors.ENDC)
	elif index == 1:
		player.choose_magic()
		magic_choice = int(input('Choose which spell:')) -1
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
			print(Bcolors.OKBLUE + '\n' + spell.name + 'deals', str(magic_dmg), 'points of damage. The enemies hp is ', str(enemy.get_hp()) + Bcolors.ENDC)

	enemy_choice = 1

	enemy_dmg = enemy.generate_damage()
	player.take_damage(enemy_dmg)
	print(Bcolors.FAIL + Bcolors.BOLD + 'Enemy attacked you for ' + str(enemy_dmg), 'points of damage. Your Hp is ' + str(player.get_hp()) + Bcolors.ENDC)

	print('-------------------------')
	print('Enemy HP: ', Bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + Bcolors.ENDC + '\n')

	print('Your HP: ', Bcolors.OKGREEN + str(player.get_hp()) + '/' + str(player.get_max_hp()) + Bcolors.ENDC)
	print('Your MP: ', Bcolors.OKBLUE + str(player.get_mp()) + '/' + str(player.get_max_mp()) + Bcolors.ENDC)

	if enemy.get_hp() == 0:
		print(Bcolors.OKGREEN + 'YOU WIN!' + Bcolors.ENDC)
		running = False
	elif player.get_hp() == 0:
		print(Bcolors.FAIL + "YOU LOOSE!" + Bcolors.ENDC)
		running = False

