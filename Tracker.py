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
						[pygame.Rect(618,20,60,260),"dining_room", True],[pygame.Rect(520,30,60,150),"kitchen", True]]


		self.dining_room = Room('dining_room', 'images/dinning_room0000.png')
		self.dining_room.exits = [[pygame.Rect(30,60,100,250),"kitchen",True],[exit_back, "hall", True]]	

		self.kitchen = Room('kitchen','images/kitchen0000.png')
		self.kitchen.exits = [[pygame.Rect(15,20,100,500),"hall",True],[exit_back, "dining_room", True]]
		# dict of all rooms 
		self.room_dict = {}

		# add all rooms to room_dict 
		self.room_dict[self.porch.room_name] = self.porch
		self.room_dict[self.hall.room_name] = self.hall
		self.room_dict[self.dining_room.room_name] = self.dining_room
		self.room_dict[self.kitchen.room_name] = self.kitchen

		""""
		TOYS AND OBJECTS 
		"""

		# instanciate all objects 
		self.key = Item("key","all_images/key0000.png",(300,400))

		# instanceate all keys 
		self.dragon = Toy("dragon","all_images/dragon0000.png",(550,330))
		self.sally = Toy("sally","all_images/Sally.png",(185,400))
		self.sally.colorkey = (255,255,255)
		self.tina = Toy("tina","all_images/Tina.png",(366,170))
		# rooms and their objects 
		self.room_junk = {
			"porch": [self.key, self.dragon], 
			"kitchen": [self.dragon,self.tina],
			"dining_room" :[self.sally],
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

	def test(self):
		return None 
