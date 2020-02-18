#cd C:\Users\Anton\Documents\GitHub\pro_eks
#cd C:\Users\Mathias Laptop\Documents\GitHub\pro_eks

import pygame
from random import randint

pygame.init()

maze_width = 8
maze_height = 8

screen = pygame.display.set_mode((maze_width * 10, maze_height * 10))
clock = pygame.time.Clock()

maze = [[0 for i in range(maze_width)] for j in range(maze_height)]
#print(maze)

def GameLoop():
	done = False

	x = 0
	y = 0
	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		
		RecursiveBacktracking(x, y)

		pygame.display.flip()
		clock.tick(600)

def RecursiveBacktracking(x, y):
	maze[x][y] = 1

	direction_possible = [False, False, False, False]
	CheckAdjacent(x, y, direction_possible)

	go = False
	while go == False:	#find en bedre måde at gøre det her på...
		value = randint(0, 3)
		if direction_possible[value] == True:
			go = True

	Move(x, y, value)


def CheckAdjacent(x, y, direction_possible):
	if y - 2 >= 0 and maze[x][y-2] == 0:
		direction_possible[0] = True
		print("North")
	if y + 2 <= maze_height and maze[x][y+2] == 0:
		direction_possible[1] = True
		print("South")
	if x + 2 <= maze_width and maze[x+2][y] == 0:
		direction_possible[2] = True
		print("East")
	if x - 2 >= 0 and maze[x-2][y] == 0:
		direction_possible[3] = True
		print("West")
	if True not in direction_possible:
		#print(maze)
		pygame.quit()
		sys.exit()
	if True in direction_possible:
		return(direction_possible)

def Move(x, y, value):
	if value == 0:
		y -= 2
	elif value == 1:
		y += 2
	elif value == 2:
		x += 2
	elif value == 3:
		x -= 2
	return(x, y)

GameLoop()