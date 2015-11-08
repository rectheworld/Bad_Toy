import pygame
import os
import math

# you will get a list as a paraemter ie list = ["ob1"]

# test list 
test_list = ["dragon"]

class Inventory():

	#SCREEN styling
	def __init__(self):
		SCREEN_WIDTH=700
		SCREEN_HEIGHT=500
		ROOM_HEIGHT=500
		self.border_color = pygame.Color("grey")
		self.border_height = 16
		self.contents = pygame.Rect(0,ROOM_HEIGHT+self.border_height/2-1,SCREEN_WIDTH,SCREEN_HEIGHT-ROOM_HEIGHT-self.border_height+1)
		self.font=game.font
		self.border_text = self.font.render("what you have:",True,pygame.color("black"),self.border_color)
		self.status = self.font.render("you are in the bank",True,pygame.color("black"),self.border_color)
		self.item=[]
		self.dirty = True

	def draw(self,screen):
		if not self.dirty:
			self.dirty = False
			screen.fill(self.contents_color,self.contents)
			pygame.draw.rect(screen,self.border_color,self.contents,self.border_height)
			screen.blit(self.border_text,(10,ROOM_HEIGHT+1))
			screen.blit(self.status,(10,SCREEN_HEIGHT-self.border_height+1))
			x = 22
			y = SCREEN_HEIGHT-self.border_height-16
			for item in self.item:   #for item in the list, call items in the dictory 

				if game.cur_item != item:
					x = item[item].inventory.update_inventory(screen,x,y)
       

        #dictionary
		objects_list = {}
		dragon_image = load_image("dragon0000.png")
		objects_list["dragon"] = dragon_image
		# do for everythibg 
		key_image = load_image("key0000.png")
		objects_list["key"]=key_image
		bear_image = load_image("Bear.png")
		objects_list["bear"] = bear_image


		# Dict of all objects 
		# dict_of_objects = {"ob1": image_variable, "ob2", image_varialbe}

		# then to access that image you will use dict_of_objects["ob1"] 



#MOUSE DRAG AND DROP  
	def mouse_click(self,pos):
		if game.is_drag:
			game.is_drag=False
			return
		x = 20
		y = SCREEN_HEIGHT-self.border_height-16
		for item in self.items:
			if items[item].inventory.disp_rect.collidepoint(pos):
				game.is_drag=True
				game.cur_item=item
				items[game.cur_item].inventory.rect[0]=pos[0]
				items[game.cur_item].inventory.rect[1]=pos[1]
				allsprites.add(items[game.cur_item].inventory,layer=2)
				break
	def mouse_motion(self,pos):
		items[game.cur_item].inventory.rect[0]=pos[0]
		items[game.cur_item].inventory.rect[1]=pos[1]
		self.dirty=True

	def mouse_release(self,pos):
		game.is_drag=False
		allsprites.remove(items[game.cur_item].inventory)
		if pos[1] <=ROOM_HEIGHT:
			game.cur_room.use(game.cur_item)
		game.cur_item=""
		self.dirty=True







		