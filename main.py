#cd C:\Users\Anton\Documents\GitHub\pro_eks
#cd C:\Users\Mathias Laptop\Documents\GitHub\pro_eks

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

def GameLoop():
	done = False

	maze[current.x][current.y] = 1
	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		
		direction_possible = [False, False, False, False]
		CheckAdjacent(direction_possible)

		while True not in direction_possible:
			if current.x == x_start and current.y == y_start:
				print(maze)
				done = True
				sys.exit()
			else:
				Backtrack()

		go = False
		while go == False:	#find en bedre måde at gøre det her på...
			random_value = randint(0, 3)
			if direction_possible[random_value] == True:
				go = True

		MoveRandom(random_value)

		pygame.display.flip()
		clock.tick(600)


def CheckAdjacent(direction_possible):
	try:
		if maze[current.x][current.y-2] == 0: #north
			direction_possible[0] = True
	except IndexError:
		pass

	try:
		if maze[current.x][current.y+2] == 0: #south
			direction_possible[1] = True
	except IndexError:
		pass

	try:
		if maze[current.x+2][current.y] == 0: #east
			direction_possible[2] = True
	except IndexError:
		pass

	try:
		if maze[current.x-2][current.y] == 0: #west
			direction_possible[3] = True
	except IndexError:
		pass

	return direction_possible 

def Backtrack():
	try:
		if maze[current.x][current.y-2] == 1:
			current.y -= 2
			print('backtracked')
	except IndexError:
		pass

	try:
		if maze[current.x][current.y+2] == 1:
			current.y += 2
			print('backtracked')
	except IndexError:
		pass

	try:
		if maze[current.x+2][current.y] == 1:
			current.x += 2
			print('backtracked')
	except IndexError:
		pass

	try:
		if maze[current.x-2][current.y] == 1:
			current.x -= 2
			print('backtracked')
	except IndexError:
		pass

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
	print('moved')

GameLoop()