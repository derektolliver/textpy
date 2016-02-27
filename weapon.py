from enum import Enum
import random

class Weapon:

	# instance variables
	# name - name of weapon
	# damage - string of weapon as int

	# weapon type enum
	Type = Enum('Type', 'Sword Dagger')

	def weapon(self, title, kind):
		self.name = title
		self.type = kind
		self.damage = random.random()

	def attack(target):
		target.health -= damage
