import pygame
import os
clock = pygame.time.Clock()
white = (255,255,255)
gameDisplay = pygame.display.set_mode((700,500))
pygame.display.set_caption('scary')

gameExit = False

current_room =  pygame.image.load(os.path.join("all_images","Porch0000.png")).convert()
key = pygame.image.load(os.path.join("all_images","key0000.png")).convert()
dragon = pygame.image.load(os.path.join("all_images","dragon0000.png")).convert()

color = key.get_at((0,0))
key.set_colorkey(color)
color1 = dragon.get_at((0,0))
dragon.set_colorkey(color1)
gameDisplay.blit(current_room,(0,0))

#self.surface.get_rect() gets the location of the surface/image


gameDisplay.blit(key,(300,400))
gameDisplay.blit(dragon,(550,330))
pygame.display.flip()
gameDisplay.fill(white)
clock.tick(60)



while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		else:
			print event

class Game(object):
	def __init__(self):
		self.game_over = False


class tracker():
	def __init__(self):
		self.ur_items_list = pygame.sprite.Group()
		self.items_location = []
		self.room_with_exits = ["porch",(270,0,180,320)]

		self.porch = Room("room","all_images/Porch0000.png")

		self.key = Item("item","all_images/key0000.png",(300,400))
		self.dragon = Item("item","all_images/dragon0000.png",(550,330))
	

		
class Room():

	def __init__(self,image_file,exit_list):
		self.exits = [(0,0,0,0)]
		

class Item(pygame.sprite.Sprite):
	def __init__(self,image_file,location):
		pygame.sprite.Sprite.__init__(self)
		self.held = False
		self.loc = location
		self.image = image_file
	def get_image(self):
		return self.image
	def get_size(self):
		return self.size
	def set_loc(self,location):
		self.loc = location


class Toys(pygame.sprite.Sprite):
	def __init__(self,image_file,loc):
		pygame.sprite.Sprite.__init__(self)
		self.image = image_file
		self.loc = location
		self.size = size
	def get_image(self):
		return self.image
	def get_size(self):
		return self.size
	def set_loc(self,location):
		self.loc = location

	def sayings(self):
		print "hello"




