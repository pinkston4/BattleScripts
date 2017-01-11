from classes.game import Person, Bcolors

magic = [{'name': 'fire', 'cost': 15, 'damage': 90},
		 {'name': 'thunder', 'cost': 5, 'damage': 70},
		 {'name': 'blizzard', 'cost': 10, 'damage': 50}]

player = Person(500, 65, 60, 35, magic)
enemy = Person(825, 65, 40, 25, magic)

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
		print('You attacked for', dmg, ' points of damage. Enemy Hp is ', enemy.get_hp())
	elif index == 1:
		player.choose_magic()
		magic_choice = int(input('Choose which spell:')) -1
		magic_dm = player.generate_spell_damage(magic_choice)
		spell = player.get_spell_name(magic_choice)
		cost = player.get_spell_mp(magic_choice)
		current_mp = player.get_mp()

		if cost > current_mp:
			print(Bcolors.FAIL + '\nNot enough magic points!' + Bcolors.ENDC)
			continue
		else: 
			enemy.take_damage(magic_dm)
			print('you used', spell, 'and inflicted', magic_dm, 'points of damage the enemies hp is ', enemy.get_hp())

	enemy_choice = 1

	enemy_dmg = enemy.generate_damage()
	player.take_damage(enemy_dmg)
	print('Enemy attacked you for ', enemy_dmg, 'points of damage. Your Hp is', player.get_hp())

	if enemy.get_hp() == 0:
		print(Bcolors.OKGREEN + 'YOU WIN!' + Bcolors.ENDC)
		running = False
	elif player.get_hp() == 0:
		print(Bcolors.FAIL + "YOU LOOSE!" + Bcolors.ENDC)
		running = False

