# cd C:\Users\Anton\Documents\GitHub\pro_eks
# cd C:\Users\anton_mc03yx6\Documents\GitHub\pro_eks
# cd C:\Users\Mathias Laptop\Documents\GitHub\pro_eks

import pygame
import sys
from random import randint

pygame.init()

maze_width = 17
maze_height = 17

screen = pygame.display.set_mode((maze_width * 10, maze_height * 10))
clock = pygame.time.Clock()

maze = [[0 for i in range(maze_width)] for j in range(maze_height)]

x_start = 1
y_start = 1

class current(object):  
    x = x_start
    y = y_start
    def __init__(self, x, y):
    	self.x = x
    	self.y = y

def GenerateMaze():
	done = False
	steps = 0
	backwards = False
	maze[current.x][current.y] = 1
	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		direction_possible = [False, False, False, False]
		CheckAdjacent(direction_possible, backwards)

		if True not in direction_possible:
			backwards = True
			CheckAdjacent(direction_possible, backwards)
		else:
			backwards = False

		go = False
		while go == False:	#find en bedre måde at gøre det her på...
			random_value = randint(0, 3)
			if direction_possible[random_value] == True:
				go = True

		MoveRandom(random_value)
		print(maze)

		pygame.display.flip()
		clock.tick(600)

		steps += 1
		if steps > maze_height * maze_width:
			sys.exit()


def CheckAdjacent(direction_possible, backwards):
	try:
		if current.y-2 >= 0 and maze[current.x][current.y-2] == backwards: #north
			direction_possible[0] = True
	except IndexError:
		print("IndexError")

	try:
		if current.y+2 <= maze_height and maze[current.x][current.y+2] == backwards: #south
			direction_possible[1] = True
	except IndexError:
		print("IndexError")

	try:
		if current.x+2 <= maze_width and maze[current.x+2][current.y] == backwards: #east
			direction_possible[2] = True
	except IndexError:
		print("IndexError")

	try:
		if current.x-2 >= 0 and maze[current.x-2][current.y] == backwards: #west
			direction_possible[3] = True
	except IndexError:
		print("IndexError")

	if backwards == True:
		print("Backtraced")
	else:
		print("Forward")

	return direction_possible 

def MoveRandom(random_value):
	if random_value == 0:
		for i in range(2):
			current.y -= 1
			maze[current.x][current.y] = 1
	elif random_value == 1:
		for i in range(2):
			current.y += 1
			maze[current.x][current.y] = 1
	elif random_value == 2:
		for i in range(2):
			current.x += 1
			maze[current.x][current.y] = 1
	elif random_value == 3:
		for i in range(2):
			current.x -= 1
			maze[current.x][current.y] = 1	

GenerateMaze()