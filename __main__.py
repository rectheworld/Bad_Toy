# BAD TOY:
# One of the Toys is Bad, Can you Tell Which One?
# Developer: Ren, Yeifi, Olivia, Lydia 
# Date: 11-07-2015

import pygame
# WILL IMPORT THESE WHEN THEY ARE BUILT 
from Tracker import tracker 

# This shouldnet go here 
from inventory import Inventory
# from room_change import Room_Change 
# from menu import Menu


FPS = 60 
SCREEN_SIZE = (700, 500)

# Main Game Class 
class Game(object):
	"""
	Main Game object of the Game. This class holds the 
	pygame screen and clock aspects. Infomation about the player is 
	imported into this class. 

	Parameters
	----------
	screen_size: A tuple object representing the size of the screen in 
		pixals (note: the order of the tuple is (y, x))

	fps: "Frames per Second". A number representing how often the game 
		screen should be refreshed 
	"""

	def __init__(self, screen_size, fps):

		pygame.init()
		self.screen_size 	= screen_size
		self.fps 			= fps 

		# Create the Pygame Screen Objects 
		self.screen 		= pygame.display.set_mode(self.screen_size)

		#Clock 
		self.clock 			= pygame.time.Clock()

		# While this variable is true, the game will continue to Run 
		self.running		= True 



		# instance of Tracker Class
		self.tracker = tracker() 

		# Keep track of what room we are in 
		# Porch is the first room we are in 
		self.current_room_string	= "porch" 
		self.current_room = self.tracker.room_dict[self.current_room_string]

		# List of things in Menu 

		# this should be connected to Tracker 
		self.inventory = Inventory() 

		# List of things in current room 
		self.tracker.room_junk[self.current_room_string]

	def room_change(self):
		pass


	def process_events(self):
		pass 	

	def render(self):
		"""
		This is the main "Speak" feature of the game. 
		it draaws the player, map, npc's to the screen

		Parameters
		----------
		None

		This function is called in the main function 
		"""

		self.screen.blit(self.current_room.image, (0,0))

		# some of this should go in think 
		for thing in self.tracker.room_junk[self.current_room_string]:
			if thing != None:
				self.screen.blit(thing.image, thing.pos)

		self.inventory.draw(self.screen)

	def main(self):
		"""
		This is the main game loop of the game. 
		It will run continiously until the player closes the screen 
		"""
		while self.running:
			events = pygame.event.get()

			# Listen for an Exit
			for event in events:
				if event.type == pygame.QUIT:
					self.running = False
					
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					print mouse_pos
					new_current_room_string = self.current_room.exit(mouse_pos)
					# Check to see if room change 
					if self.current_room_string != new_current_room_string:
						self.current_room_string = new_current_room_string
						self.current_room = self.tracker.room_dict[self.current_room_string]

			self.screen.fill((255, 0,255))

			self.process_events()

			self.render()

			pygame.display.flip()

			self.clock.tick(FPS)

		pygame.quit()


if __name__== "__main__":
	game = Game(SCREEN_SIZE, FPS)
	game.main()


