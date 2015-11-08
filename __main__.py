# BAD TOY:
# One of the Toys is Bad, Can you Tell Which One?
# Developer: Ren, Yeifi, Olivia, Lydia 
# Date: 11-07-2015

import pygame

# WILL IMPORT THESE WHEN THEY ARE BUILT 

# from tracker import Tracker 
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

		# Keep track of what room we are in 
		self.current_room	= None 


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
		pass 

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
					pygame.quit()

			self.screen.fill((255, 255,255))

			self.process_events()

			self.render()

			self.clock.tick(FPS)


if __name__== "__main__":
	game = Game(SCREEN_SIZE, FPS)
	game.main()


