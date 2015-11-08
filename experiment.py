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







