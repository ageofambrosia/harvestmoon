from sys import exit
from random import randint 
import random


def seeds(field_type):
			
	seed_cost, seed = crop_cost()								# returns the seed cost
	planting_fertility = plant(seed)							# returns fertility based on sow time
	crop_group = crop_type(seed)								# returns the crop group (root, fruit, or leaf)
	crop_rotation = soil_content_test(crop_group, field_type)	# returns fertility based on crop rotation
																# (i.e. fertility based on previous season's crop type)
	return seed_cost, planting_fertility, seed, crop_group, crop_rotation
	
	
def crop_type(crop):					# designates crops as root, fruit, or leaf bearing
	
	if crop == "onion" or crop == "carrot":
		crop_group = "root"
	elif crop == "corn" or crop == "wheat":
		crop_group = "fruit"
	elif crop == "lettuce" or crop == "broccoli":
		crop_group = "leaf"
	else:
		print "Something went wrong!"
	return crop_group
		
		
def crop_cost():
	a = 0
	
	while a < 3:
		
		crop = raw_input("Pick a seed (onion, carrot, corn, wheat, lettuce, broccoli): ")
		seed = crop.capitalize()
		
		if crop == "onion" or crop == "wheat" or crop == "lettuce":
			input = raw_input("\n%s seeds cost $2. Press 'buy' to purchase or 'menu'"
			" to return to the main menu: " % seed)
			
			if input == "buy":
				cost = 2						# sets the cost of onion, wheat, and lettuce seeds to $2
				return cost, crop
			elif input == "menu":
				seeds()
			else:
				print "Learn to type, dude."
				exit(0)
				
		elif crop == "carrot" or crop == "corn" or crop == "broccoli":
			input = raw_input("\n%s seeds cost $3. Press 'buy' to purchase or 'menu'"
			" to return to the main menu: " % seed)
			
			if input == "buy":
				cost = 3						# sets the cost of carrot, corn, and broccoli seeds to $3
				return cost, crop
			elif input == "menu":
				seeds()
			else:
				print "Learn to type, dude."
				exit(0)
				
		else:
			
			if a < 2:
				print "\nDo you know how to type, bruh? Try again\n"
			else:
				print "\nYou suck at typing. Go away.\n"
		
		a = a + 1
	
	exit(0)

	
def plant(crop):
	sow = raw_input("\nWhen do you want to sow your seeds"
	" (early spring, mid-spring, late spring)?: ")
	
	if crop == "onion" or crop == "wheat":
	# ideally, these crops should be planted in mid-spring	
		if sow == "early spring":
			field_quality = 0
		elif sow == "mid-spring":
			field_quality = 1
		elif sow == "late spring":
			field_quality = 0
		else:
			print "\nGo to typing school.\n"
			exit(0)
			
	elif crop == "carrot" or crop == "lettuce" or crop == "broccoli":
	# ideally, these crops should be planted in early spring	
		if sow == "early spring":
			field_quality = 1
		elif sow == "mid-spring":
			field_quality = 0
		elif sow == "late spring":
			field_quality = -1
		else:
			print "\nGo to typing school.\n"
			exit(0)
			
	elif crop == "corn":
	# ideally, this crop should be planted in late spring	
		if sow == "early spring":
			field_quality = -1
		elif sow == "mid-spring":
			field_quality = 0
		elif sow == "late spring":
			field_quality = 1
		else:
			print "\nGo to typing school.\n"
			exit(0)
			
	else:
		print "\nYou're an attrocious typer.\n"
		exit(0)
		
	return field_quality


def fertilizer():
	fertilizer = raw_input("\nPick your fertilizer (none, organic [$2], chemical [$1]): ")
	
	if fertilizer == "none":
		return (0,0)				# 0 is fertilizer addition, 0 is cost in dollars
	elif fertilizer == "organic":
		return (1,2)				# 1 is fertilizer addition, 2 is cost in dollars
	elif fertilizer == "chemical":
		return (randint(-1,2),1)	# random integer for fertilizer addition, 1 is cost in dollars
	else:
		print "\nUgh, go to typing school!\n"
		exit(0)

		
def grow(soil):						# determines output based on field fertility
	
	if random.random() < 0.9:
	
		if soil <= 0:
			crop_yield = 0
		elif soil == 1 or soil == 2:
			crop_yield = 1
		elif soil == 3 or soil == 4:
			crop_yield = 2
		else:
			crop_yield = 3
			
	else:
		print "\nYour crop has been hit with an infestation. Bye-bye crops!\n"
		crop_yield = 0
	return crop_yield


def soil_content_test(last_season, this_season):	# crop rotation provides further field fertility
	
	if last_season == this_season:
		fertility = 0
		return fertility
	else:
		fertility = 1
		return fertility


def random_disaster():
		if random.random() <= 0.1:
			print "Early rains flood your fields! Your field's fertility drops by 2!\n"
			field_fertility = 4
		elif 0.1 < random.random() <= 0.2:
			print "Other farmers sabotage your field! Your field's fertility drops by 3!\n"
			field_fertility = 5
		elif 0.2 < random.random() <= 0.3:
			print "Someone pissed on your field and the pH is off the charts! Your"
			"field's fertility drops by 1!\n"
			field_fertility = 3
		elif 0.3 < random.random() <= 0.4:
			print "Someone infected with the bubonic plague coughed all over your soil!"
			"Your field's fertility drops by 4!\n"
			field_fertility = 5
		else:
			field_fertility = 0
		return field_fertility
		
def acct():
	# starting amount of money ($10)
	bank = 10
	
	# randomly chooses a field quality (0-2, higher numbers represent more fertility)
	field = [0, 0]
	field[0] = randint(0,2)
	
	while 15 > bank > 0:
		print "\nAll right, here goes the season!\n"
		field[0] = field[0] - random_disaster()
		print "Your field fertility: %d" % field[0]
		
		# assigns additional field quality based on fertilizer choice
		# assigns to fertilizer_cost the cost of the fertiziler (if any)
		addition, fertilizer_cost = fertilizer()
		bank = bank - fertilizer_cost
		if bank < 0:
			break
		field[0] = field[0] + addition
		
		print "The fertilizer cost: $%d" % fertilizer_cost
		print "You have $%d in your bank now.\n" % bank
		print "The fertility addition to the field: %d" % addition
		print "The field's total fertility: %d\n" % field[0] 
			
		# returns the seed cost, the additional field quality based on sow time,
		# the seed name, and the plant type (root, fruit, leaf)
		seed_cost, sow_addition, seed_name, plant_type, fertility_crop_type = seeds(field[1])
		field[1] = plant_type
		bank = bank - seed_cost
		if bank < 0:
			break
		field[0] = field[0] + sow_addition + fertility_crop_type
		
		print "You have $%d in your bank now.\n" % bank
		print "The fertility addition to the field: %d" % (sow_addition + fertility_crop_type)
		print "The field's total fertility: %d\n" % field[0]
		
		# returns the crop yield and calculates the profit from that
		# adds the profit to the bank account
		crop_yield = grow(field[0])
		profit = crop_yield * seed_cost
		bank = bank + crop_yield * seed_cost
		if bank < 0:
			break
		
		raw_input("Press any key to find out what happens . . .\n")
		print "Your crop yield is %d times your input. You made $%d." % (crop_yield, profit)
		print "You now have $%d in your account." % bank
	
	if bank <= 0: 
		print "\nYou have no money left, primarily because you suck. Game over.\n"
	else:
		print "\nYou won!\n"
	exit(0)

acct()