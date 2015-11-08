import pygame
"""
This is the toy class. 
It will represent all the
same catigories for all the toys.
"""
class Item(pygame.sprite.Sprite):
	"""
	Paramerers: 
	---------
	obj_name = This is name of the item.
	loc = This will be a tuple that has the pixal location/size. it will initialize where is located in an image.
	held = This will determine if the item has been picked up or not.
	"""
	def __init__(self, obj_name, image_file,loc_and_size):
		pygame.sprite.Sprite.__init__(self)
		self.obj_name = obj_name
		self.held = False # lets us know wither the item has been picked up.
		self.loc = loc_and_size
		self.image = image_file
		# All get and set methods will either get or set the the specific catigory of that toy
	def get_image(self):
		return self.image
	def get_size(self):
		return self.loc_size
	def set_loc(self,loc_and_size):
		self.loc_size = loc_and_size



	def __init__(self, obj_name, image_file,loc_and_size):
		pygame.sprite.Sprite.__init__(self)
		self.image = image_file
		self.loc_size = loc_and_size
	
	def get_image(self):
		return self.image
	def get_loc(self):
		return self.loc_size
	def set_loc(self,location):
		self.loc_size = loc_and_size
	# This represents the things that the toys might say to the player.
	def sayings(self,strings):
		print strings

