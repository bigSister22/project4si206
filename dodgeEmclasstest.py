import pygame
import time
import random
import os

pygame.init()

###################### colors #########################
BLACK = (0,0,0)
GOBLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)

###################### display dimensions #########################
display_width = 800
display_height  = 600

###################### set up #########################
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Slither')



clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)

def message(msg,color):
	screen_text = font.render(msg,True,color)
	gameDisplay.blit(screen_text,[display_width/2,display_height/2]) 

def gameLoop():
##################### Boolian Play values #########################
	gameExit = False
	gameOver = False


##################### display dimensions #########################
	lead_x = display_width/2
	lead_y = display_height/2

	lead_x_change = 0
	lead_y_change = 0



	randSX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
	randSY = round(random.randrange(0, display_height-block_size)/10.0)*10.0



	randImX = (random.randrange(0, display_width-block_size))
	randImY = (random.randrange(0, display_height-block_size))


	ball = pygame.image.load(os.path.join('images', 'ball.bmp'))

	while not gameExit:
		while gameOver == True:
			gameDisplay.fill(WHITE)
			message("Failed. Press C to play again, Q to quit", GOBLUE)
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
			
		lead_x += lead_x_change
		lead_y += lead_y_change




		gameDisplay.fill(WHITE)
		pygame.draw.rect(gameDisplay, GREEN,[randSX, randSY,block_size,block_size])
		gameDisplay.blit(ball, (randImX, randImY))
		pygame.draw.rect(gameDisplay, GOBLUE, [lead_x,lead_y,block_size,block_size])
		
		pygame.display.update()
		
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