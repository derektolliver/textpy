from enum import Enum
import random

class Weapon:

	# instance variables
	name;
	damage;

	# weapon type enum
	Type = Enum('Type', 'Sword Dagger')

	def f(self, title, kind):
		self.name = title;
		self.type = kind;
		damage = random.random()

	def attack():

