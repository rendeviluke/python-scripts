import pygame, random
from pygame.locals import *

def on_grid_random():
	x = random.randint(0, 590)
	y = random.randint(0, 590)
	return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
	return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
r = 4

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snakeSkin = pygame.Surface((10,10))
snakeSkin.fill((255, 255, 255))



applePos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255, 0, 0))

myDirection = LEFT

clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

gameover = False

while not gameover:
	clock.tick(20)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

		if event.type == KEYDOWN:
			if event.key == K_UP:
				myDirection = UP
			if event.key == K_DOWN:
				myDirection = DOWN
			if event.key == K_LEFT:
				myDirection = LEFT
			if event.key == K_RIGHT:
				myDirection = RIGHT
			
	if collision(snake[0], applePos):
		applePos = on_grid_random()
		snake.append((0,0))
		score = score + 1

	if snake[0][0] == 600 or snake [0][0] < 0 or snake[0][1] < 0:
		gameover = True
		break

	for i in range(1, len(snake) - 1):
		if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
			gameover = True
			break
	if gameover:
		break

	for i in range(len(snake) - 1, 0, -1):
		snake[i] = (snake[i-1][0], snake[i-1][1])

	if myDirection == UP:
		snake[0] = (snake[0][0], snake[0][1] - 10)
	if myDirection == DOWN:
		snake[0] = (snake[0][0], snake[0][1] + 10)
	if myDirection == RIGHT:
		snake[0] = (snake[0][0] + 10, snake[0][1])
	if myDirection == LEFT:
		snake[0] = (snake[0][0] - 10, snake[0][1])		

	screen.fill((0,0,0))
	screen.blit(apple, applePos)



	score_font = font.render('Score: %s' % (score), True, (255,255,255))
	score_rect = score_font.get_rect()
	score_rect.topleft = (600 - 120, 10)
	screen.blit(score_font, score_rect)

	for pos in snake:
		screen.blit(snakeSkin, pos)

	pygame.display.update()

if gameover == True:
	gameover_font = pygame.font.Font('freesansbold.ttf', 75)
	gameover_screen = gameover_font.render('Game Over', True, (255,255,255))
	gameover_rect = gameover_screen.get_rect()
	gameover_rect.midtop = (600 / 2, 10)
	screen.blit(gameover_screen, gameover_rect)
	pygame.display.update()
	pygame.time.wait(500)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()