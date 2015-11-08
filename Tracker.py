class tracker():
	def __init__(self):
		self.ur_items_list = pygame.sprite.Group()
		self.items_location = []

		self.room_with_exits = ["porch",(270,0,180,320)]

		# Instanceinate all rooms
		# Include Exits 

		self.porch = Room("porch","all_images/Porch0000.png")
		#self.porch.exit.append KDskfjdslfjds;lfk;sd

		self.kitchen

		# instanciate all objects 
		self.key = Item("key","all_images/key0000.png",(300,400))

		# instanceate all keys 
		self.dragon = Item("dragon","all_images/dragon0000.png",(550,330))
	
		# rooms and their objects 
		self.dict_thing = {
			"porch": [self.key, self.dragon], 
			"Kitchen": [self.bear],
		}

		# Menu object 
		# list of strings list = ["dragon", "key", "Tina"]
		# ie object.obj.name 

	def update_room_poosenson(self, key_of_onject_in_dict):
		pass
		# updates the where objects are in each roo,

	def update_inventory():
		# updates the list of strings that are passed to yeifi and are used for the emnu 
		pass 

