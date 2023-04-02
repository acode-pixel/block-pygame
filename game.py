import pygame 
import sys
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
rectangle_rect = (200, 200, 50, 50)
color = (255, 255, 255)
text_color = (255, 255, 255)
background_color = (0, 0, 0)
score = 0
font = pygame.font.Font("font/game.otf", 40)
pygame.mixer.music.load("sound/blipSelect.wav")
running = True 

while running: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if rectangle.collidepoint(pos) == True:
				score += 1
				pygame.mixer.music.play()
				rectangle_rect = (random.randint(0, 350), random.randint(0, 350), 50, 50)
				color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
		if score == 10:
			background_color = (255, 255, 255)
			text_color = (0, 0, 0)

		text = font.render(str(score), True, text_color)
		text_rect = text.get_rect(topleft=(185, 10))
		screen.fill(background_color)
		screen.blit(text, text_rect)
		rectangle = pygame.draw.rect(screen, color, rectangle_rect)
		pygame.display.update()


