'''
Nick Boni
7/23/2018

This file defines the Person class, upon which all
human characters in the game are based.
'''

from creature import *
from mechanics import battle, determine_response

names = ['Mattias','Franny','Leopold','Catche','Slan','Reog',
'Frack','Lance','Samantha','Lili','Martha','Zuzu','Borb','Horatio',
'Rosecratz','Guildenstern','Chunk','Blork','Effel','Yorick', 'Puck',
'Osgood','Rank','Lelel','Bilbo','Kattiwampus']

#################################################################
#################################################################
#################################################################

class Person(Creature):

	def __init__(
		self,
		name='',
		faction=None,
		allegiance=0
		):

		Creature.__init__(self,
					name = name)
		
		self.faction = faction
		self.allegiance = allegiance

#################################################################

	def generate_stats(self,hero):

		self.LEVEL = randint(hero.LEVEL-10,hero.LEVEL+10)

		if self.LEVEL <= 0:
			self.LEVEL = 1

		self.EXP = randint( 0, self.determine_exp()-1 )
		self.MAXHP = 10 + ( (self.LEVEL-5) * randint(0,3) )
		self.HP = self.MAXHP
		self.ATK = self.LEVEL + randint(-10,10)
		self.DEF = self.LEVEL + randint(-10,10)
		self.SPD = self.LEVEL + randint(-10,10)
		self.LCK = self.LEVEL + randint(-10,10)
		self.SNK = self.LEVEL + randint(-10,10)
		self.CHM = self.LEVEL + randint(-10,10)
		self.INT = self.LEVEL + randint(-10,10)
		if self.name == '':
			self.name = choice(names)

		# Intelligence is charming!
		self.CHM += (self.INT / 2)

		self.check_attrs()

#################################################################

	def chat(self,other):
		'''Chatting with generic Persons is boring.'''

		responses = ['I am extremely ugly.',
		'Dost thou smell that?',
		'I have chopped down one thousand trees in my life.',
		'Wilt thou scratch mine buttocks?',
		'Thou art a stump.',
		'Inspectum mine rectum.',
		"I shall cavort for thee! Wait, no, don't run away!"]

		response = '\n%s: '%self.name + choice(responses) + '\n'

		print(response)

#################################################################

	def test_convo(self,other,instr):
		'''User input validation for conversations with the person.'''
		action = input(instr).lower()

		if not (action == 'y' or action == 'n'):
			print('\nThou hast not answered the question!')
			self.chat(other)

		return action

#################################################################

	def get_factional_opinion(self, other):
		'''
		Accepts Person object as input.

		Checks Other's factional association,
		compares it to self's factional assocation.

		Returns float between -1 and 1.
		'''

		return(self.faction.opinion(other))

#################################################################

if __name__ == '__main__':

	from faction import *

	Romans = Faction('Romans')
	Huns = Faction('Huns')

	Romans.opinions = {Huns: -1}
	Huns.opinions = {Romans: -0.9}

	roman = Person('dookie',Romans,0.3)
	hun = Person('smirkle',Huns,0.9)

	print(f"Roman's opinion of Hun: {roman.get_factional_opinion(hun)}")

	'''

	from mechanics import load_file
	from item import Item

	hero = load_file()

	x = Person('doofus')
	print('\n %s'%x.name)
	print(x.gen_stats_string())

	hero = load_file()

	h = Item('hotdog')
	r = Item('rock')

	choice = input('Which item wilt thou take? Type 1 for hotdog, 2 for rock')
	if choice == '1':
		hero.inventory.append(h)
	elif choice == '2':
		hero.inventory.append(r)
	else:
		print('You fool!')

	print(hero.inventory)

	for item in hero.inventory:
		print(item.name)	

	# y = Peasant(hero,'roofdus')
	# print('\n %s'%y.name)
	# print(y.gen_stats_string())

	# a = Archer(hero,'Borkus')
	# print('\n %s'%a.name)
	# print(a.gen_stats_string())

	# wiz = Wizard(hero)
	# print('\n %s'%wiz.name)
	# print(wiz.gen_stats_string())

	# e = Elder(hero)
	# print('\n %s'%e.name)
	# print(e.gen_stats_string())

	# war = Warrior(hero)
	# print('\n %s'%war.name)
	# print(war.gen_stats_string())



	print(x.name)
	print(x.gen_stats_string())

	# print(a.name)
	# print(a.gen_stats_string())

	# print(wiz.name)
	# print(wiz.gen_stats_string())

	# print(war.name)
	# print(war.gen_stats_string())

	# if input('Wilt thou chat with %s? '%a.name) == 'y':
	# 	a.chat(hero)

	# if input('Wilt thou chat with %s? '%e.name) == 'y':
	# 	e.chat(hero)

	'''