import pygame

#This is your class Olivia  
#from room_logic import Room_Logic
	
class Room():

	def __init__(self,room_name, image_file,exit_list = None):
		""""
		self.exits holds the tupis Ie ________________
		Add bottom exits 

		"""
		self.room_name = room_name
		self.image = pygame.image.load(image_file).convert()
		self.rect			= self.image.get_rect()

		"""
		This is a list of lists, where each of the mini lists has the format:
		[<rect_object in tuple>, <the room this door leads to as a string>, <Wheather that room is accessible True/ False ]

		"""
		self.exits = []
		

	def exit(self, mouse_pos):
		"""
		This fucntion is called in main to test is the player has clicked on a door 

		Parameters
		----------
		mouse_pos - Tuple of two ints returned by the event lisenters in main 

		Returns
		----------
		A string representing te name of the  next room to be displayed 

		"""
		for rect in self.exits:
			# rect[0] is the rect object
			if rect[0].collidepoint(mouse_pos) == True:
				# rect[1] is te name of the next room as a string 
				if rect[2] == True:
					next_room = rect[1]
					return next_room
				else:
					# Some function to test wheather that code is accessible 
					# assume you have access to player's inventor which is a list of strings, ie = ['dragon', 'key']
					# Take in (self) as a parameter as a staring node 
					# returns true or false 
					# if some fucntion returns true:
					######rect[2] = True 
					######next_room = rect[1]
					######return next_room

					# Ren 
					# This function wont go here, it will tell main to walk the tree and then promt 
					#exits(again based on the result )
		return self.room_name
