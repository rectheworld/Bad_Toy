import pygame
from Room import Room
from Toy import Toy 
from Items import Item


class tracker():
	def __init__(self):
		self.ur_items_list = pygame.sprite.Group()
		self.items_location = []

		exit_back = pygame.Rect(0,430,500,70)

		"""
		Rooms

		Instanciate all rooms and there exits
		"""
		self.porch = Room("porch","images/Porch0000.png")
		# porch esits 
		porch_exit_to_hall = pygame.Rect(265, 0, 185, 320)
		self.porch.exits.append([porch_exit_to_hall, "hall", True])

		self.hall = Room("hall", "images/stairs0000.png")
		# hall exits
		self.hall.exits = [[exit_back, "porch", True], 
						[pygame.Rect(618,20,60,260),"dining_room", True] ]


		self.dining_room = Room('dining_room', 'images/dinning_room0000.png')
		self.dining_room.exits = [[exit_back, "hall", True]]	

		# dict of all rooms 
		self.room_dict = {}

		# add all rooms to room_dict 
		self.room_dict[self.porch.room_name] = self.porch
		self.room_dict[self.hall.room_name] = self.hall
		self.room_dict[self.dining_room.room_name] = self.dining_room

		""""
		TOYS AND OBJECTS 
		"""

		# instanciate all objects 
		self.key = Item("key","all_images/key0000.png",(300,400))

		# instanceate all keys 
		self.dragon = Toy("dragon","all_images/dragon0000.png",(550,330))

		# rooms and their objects 
		self.room_junk = {
			"porch": [self.key, self.dragon], 
			"Kitchen": [self.dragon],
			"dining_room" :[],
			"hall" :[]
		}

		# Menu object 
		#self.menu_list = ["dragon"]
		# ie object.obj.name 

	def update_room_poosenson(self, key_of_onject_in_dict):
		pass
		# updates the where objects are in each roo,

	def update_inventory():
		# updates the list of strings that are passed to yeifi and are used for the emnu 
		pass 

