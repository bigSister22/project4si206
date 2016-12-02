

# The objective of this assignment is to show that you can create (on your own) a Python program that uses modules, classes, and event detection.You can import/use any pygame modules but everything must be your own code.  

# A:  Create a variation of PacMan, Breakout, Asteroids.    You can create a game of your choice, but it must include movement, collision detection, scoring and/or time, and animation. 

################### All games should include sound. Base score is 100/150 pts for a working game.

# B: Show at least two consistent weeks of commits (at least 10 different days, more than 5 hours apart) 10pts

################## C: Demonstrate a unique implementation of Class Inheritance 10pts

# D: Final 30 points are on a curved scale.  The class will rank the best games in the class.

# Scoring breakdown (out of 150)

# working game: 100pts

# version control: 10pts

# class inheritance/create your own subclass: 10pts
##################
#figure out how to make image a rect and use the collison fucntion to subtract lives
###################
import pygame
import time
import random
import os

pygame.init()

pygame.display.set_caption('DodgeEm!!')

class EndMessage():

	def end_message(self,msg,score,color):
		screen_text = self.font.render((msg+str(score)),True,color)
		self.gameDisplay.blit(screen_text,[self.display_width/4,self.display_height/2])

class GameElements(EndMessage):
	clock = pygame.time.Clock()

	BLACK = (0,0,0)
	GOBLUE = (0, 0, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	WHITE = (255,255,255)

	display_width = 800
	display_height  = 600

	block_size = 10
	FPS = 30

	font = pygame.font.SysFont(None, 25)
	def __init__(self):

		self.clock = self.clock

		self.BLACK = self.BLACK
		self.GOBLUE = self.GOBLUE
		self.RED = self.RED
		self.GREEN = self.GREEN
		self.WHITE = self.WHITE

		self.display_width = self.display_width
		self.display_height  = self.display_height

		self.block_size = self.block_size
		self.FPS = self.FPS

		self.font = self.font

	def gameDisplay(self):
		self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))


	 ###mmm### lead_x and y might need to be what variable is and not name

	def lives_message(self,msg,lives,color):
		screen_text = self.font.render((msg+str(lives)),True,color)
		self.gameDisplay.blit(screen_text,[10,10])

	def scoreMessage(self,msg,score,color):
		screen_text = self.font.render((msg+str(score)),True,color)
		self.gameDisplay.blit(screen_text,[40,40])

	def gameLoop(self):
		gameExit = False
		gameOver = False
		###############
		score = 0
		coordList = []
		lives = 3
		###############



		lead_x = self.display_width/2
		lead_y = self.display_height/2

		lead_x_change = 0
		lead_y_change = 0



		randSX = round(random.randrange(0, self.display_width-self.block_size)/10.0)*10.0
		randSY = round(random.randrange(0, self.display_height-self.block_size)/10.0)*10.0



		randImX = round(random.randrange(0, self.display_width-self.block_size)/10.0)*10.0
		randImY = round(random.randrange(0, self.display_height-self.block_size)/10.0)*10.0


		# RED square image #### ball = pygame.image.load(os.path.join('images', 'ball.bmp'))
		ball = pygame.sprite.Sprite()
		ball.image = pygame.image.load(os.path.join('images', 'ball.bmp')).convert_alpha()
		ball.rect = ball.image.get_rect()
		ball.rect.move_ip(10,10)
		ball = pygame.image.load(os.path.join('images', 'ball.bmp'))

		# BLUE square image #### ball = pygame.image.load(os.path.join('images', 'ball.bmp'))
		blueball = pygame.sprite.Sprite()
		blueball.image = pygame.image.load(os.path.join('images', 'blueball.bmp')).convert_alpha()
		blueball.rect = blueball.image.get_rect()
		blueball.rect.move_ip(10,10)
		blueball = pygame.image.load(os.path.join('images', 'blueball.bmp'))

		# Green square image #### ball = pygame.image.load(os.path.join('images', 'ball.bmp'))
		greenball = pygame.sprite.Sprite()
		greenball.image = pygame.image.load(os.path.join('images', 'greenball.bmp')).convert_alpha()
		greenball.rect = greenball.image.get_rect()
		greenball.rect.move_ip(10,10)
		greenball = pygame.image.load(os.path.join('images', 'greenball.bmp'))

		#melody = pygame.mixer.Sound.play('tomLogicProAudioFile.wav')
		# pygame.mixer.pre_init(44100, 16, 2, 4096)
		# melody = pygame.mixer.Sound(os.path.join("sounds", "tk.wav")).convert_alpha()

		#melody.play()
		
		while not gameExit:
			while gameOver == True:
				self.gameDisplay.fill(self.WHITE)
				self.end_message("No lives left!! You dead. Press C to play again, Q to quit. SCORE: ", score,self.GOBLUE)
				pygame.display.update()
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							gameExit = True
							gameOver = False
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_c:
							self.gameLoop()

			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						lead_x_change = -self.block_size
						lead_y_change = 0
					elif event.key == pygame.K_RIGHT:
						lead_x_change = self.block_size
						lead_y_change = 0
					elif event.key == pygame.K_UP:
						lead_y_change = -self.block_size
						lead_x_change = 0
					elif event.key == pygame.K_DOWN:
						lead_y_change = self.block_size
						lead_x_change = 0
			if lead_x >= self.display_width or lead_x < 0 or lead_y >= self.display_height or lead_y < 0:
				#gameOver = True
				lives-=1
				lead_x = self.display_width/2
				lead_y = self.display_height/2


			if lives == 0:
				gameOver = True

			lead_x += lead_x_change
			lead_y += lead_y_change


			
			
			self.gameDisplay.fill(self.WHITE)
			self.scoreMessage("score: ",score, self.GOBLUE)
			self.lives_message("Lives remaining: ",lives, self.GOBLUE)##### 1 ######may need to tweak funtion. lives and goblue are in a tup.. not sure if that fixed it
			#pygame.draw.rect(gameDisplay, GREEN,[randSX, randSY,block_size,block_size])
			self.gameDisplay.blit(greenball,(randSX,randSY))
			self.gameDisplay.blit(ball, (randImX, randImY))
			for x in coordList:
				self.gameDisplay.blit(ball, (x))
			#pygame.draw.rect(gameDisplay, GOBLUE, [lead_x,lead_y,block_size,block_size])
			self.gameDisplay.blit(blueball, (lead_x,lead_y))
			pygame.display.update()
			
			if lead_x == randSX and lead_y == randSY:
			#if pygame.sprite.collide_rect(blueball,greenball):
			# if greenball.colliderect(blueball):
			#if pygame.sprite.spritecollide(blueball, greenball, True):
				# print("COLLISION!!!")
				score+=1
				randSX = round(random.randrange(0, self.display_width-self.block_size)/10.0)*10.0
				randSY = round(random.randrange(0, self.display_height-self.block_size)/10.0)*10.0
				for x in range (4):
					coordList.append((round(random.randrange(0, self.display_width-self.block_size)/10.0)*10.0, round(random.randrange(0, self.display_height-self.block_size)/10.0)*10.0))


			
			if lead_x == randImX and lead_y == randImY:
				lives-=1
			for x in coordList:
				if x[0]== lead_x and x[1] == lead_y:
					lives-=1
			

			
			self.clock.tick(self.FPS)
		
		pygame.quit()
		quit()





gameref = GameElements()
gameref.gameDisplay()
gameref.gameLoop()


