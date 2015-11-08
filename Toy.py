import pygame
"""
This is the toy class. 
It will represent all the
same catigories for all the toys.
"""
class Toy(pygame.sprite.Sprite):
	"""
	Paramerers: 
	---------
	obj_name = this is name of the toy 
	loc = This will be a tuple that has the pixal location/size. it will initialize where is located in an image.
	"""
	def __init__(self, obj_name, image_file,pos):

		pygame.sprite.Sprite.__init__(self)
		self.obj_name = obj_name

		self.image = pygame.image.load(image_file).convert()
		#self.rect = pygame.Rect(pygame.get_image_rect())
		colorkey = self.image.get_at((0,0))
		self.image.set_colorkey(colorkey)
		self.pos = pos

	# All get and set methods will either get or set the the specific catigory of that toy
	def get_image(self):
		return self.image
	def get_pos(self):
		return self.loc_size
	def set_pos(self,location):
		self.pos = pos
	# This represents the things that the toys might say to the player.
	def sayings(self,strings):
		print strings

