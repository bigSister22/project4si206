# The objective of this assignment is to show that you can create (on your own) a Python program that uses modules, classes, and event detection.You can import/use any pygame modules but everything must be your own code.  

# A:  Create a variation of PacMan, Breakout, Asteroids.    You can create a game of your choice, but it must include movement, collision detection, scoring and/or time, and animation. All games should include sound. Base score is 100/150 pts for a working game.

# B: Show at least two consistent weeks of commits (at least 10 different days, more than 5 hours apart) 10pts

# C: Demonstrate a unique implementation of Class Inheritance 10pts

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

BLACK = (0,0,0)
GOBLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)

display_width = 800
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('DodgeEm!!')



clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)



def end_message(msg,score,color):
	screen_text = font.render((msg+str(score)),True,color)
	gameDisplay.blit(screen_text,[display_width/4,display_height/2]) ###mmm### lead_x and y might need to be what variable is and not name

def lives_message(msg,lives,color):
	screen_text = font.render((msg+str(lives)),True,color)
	gameDisplay.blit(screen_text,[10,10])

def gameLoop():
	gameExit = False
	gameOver = False
	###############
	score = 0
	coordList = []
	lives = 3
	###############



	lead_x = display_width/2
	lead_y = display_height/2

	lead_x_change = 0
	lead_y_change = 0



	randSX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
	randSY = round(random.randrange(0, display_height-block_size)/10.0)*10.0



	randImX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
	randImY = round(random.randrange(0, display_height-block_size)/10.0)*10.0


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
	
	while not gameExit:
		while gameOver == True:
			gameDisplay.fill(WHITE)
			end_message("No lives left!! You dead. Press C to play again, Q to quit. SCORE: ", score,GOBLUE)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						gameLoop()

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0
		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
			gameOver = True
		if lives == 0:
			gameOver = True

		lead_x += lead_x_change
		lead_y += lead_y_change


		

		gameDisplay.fill(WHITE)
		lives_message("Lives remaining: ",lives, GOBLUE)
		#pygame.draw.rect(gameDisplay, GREEN,[randSX, randSY,block_size,block_size])
		gameDisplay.blit(greenball,(randSX,randSY))
		gameDisplay.blit(ball, (randImX, randImY))
		for x in coordList:
			gameDisplay.blit(ball, (x))
		#pygame.draw.rect(gameDisplay, GOBLUE, [lead_x,lead_y,block_size,block_size])
		gameDisplay.blit(blueball, (lead_x,lead_y))
		pygame.display.update()
		
		if lead_x == randSX and lead_y == randSY:
		#if pygame.sprite.collide_rect(blueball,greenball):
		# if greenball.colliderect(blueball):
		#if pygame.sprite.spritecollide(blueball, greenball, True):
			# print("COLLISION!!!")
			score+=1
			randSX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
			randSY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
			for x in range (4):
				coordList.append((round(random.randrange(0, display_width-block_size)/10.0)*10.0, round(random.randrange(0, display_height-block_size)/10.0)*10.0))


		# if pygame.sprite.spritecollide(ball,rect):
		# 	print ("Game Over")
		if lead_x == randImX and lead_y == randImY:
			lives-=1
		for x in coordList:
			if x[0]== lead_x and x[1] == lead_y:
				lives-=1
		

		
		clock.tick(FPS)
	# message("FAIL", GOBLUE)
	# pygame.display.update()
	# time.sleep(2)
	pygame.quit()
	quit()


gameLoop()











































#########################################
# import pygame
# import os
# pygame.init()


# BLACK = (0,0,0)
# GOBLUE = (0, 0, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# WHITE = (255,255,255)


# display_width = 800
# display_height  = 600

# gameDisplay = pygame.display.set_mode((display_width,display_height))
# gameDisplay.fill(WHITE)

# pygame.display.set_caption("DodgeEm!!")

# ball = pygame.image.load(os.path.join('images', 'ball.bmp'))

# block_size = 20
# x_pos = 300
# y_pos = 300
# lead_x = display_width/2
# lead_y = display_height/2

# lead_x_change = 10
# lead_y_change = 0

# gameExit = False
# while not gameExit:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			gameExit = True
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_LEFT:
# 				direction = "left"
# 				lead_x_change = -block_size
# 				lead_y_change = 0
# 			if event.key == pygame.K_RIGHT:
# 				direction = "right"
# 				lead_x_change = block_size
# 				lead_y_change = 0
# 			if event.key == pygame.K_UP:
# 				direction = "up"
# 				lead_y_change = -block_size
# 				lead_x_change = 0
# 			if event.key == pygame.K_DOWN:
# 				direction = "down"
# 				lead_y_change = block_size
# 				lead_x_change = 0

# 	if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
# 		gameOver = True

# 	lead_x += lead_x_change
# 	lead_y += lead_y_change
# 	gameDisplay.blit(ball, (lead_x,lead_y))
# 	pygame.display.update()



# pygame.quit()
# quit()