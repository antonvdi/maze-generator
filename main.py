#cd C:\Users\Anton\Documents\GitHub\pro_eks
#cd C:\Users\Mathias Laptop\Documents\GitHub\pro_eks

import pygame
import sys
from random import randint

pygame.init()

maze_width = 7
maze_height = 7

screen = pygame.display.set_mode((maze_width * 10, maze_height * 10))
clock = pygame.time.Clock()

maze = [[0 for i in range(maze_width)] for j in range(maze_height)]

class current(object):  
    x = 1
    y = 1
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
		
		RecursiveBacktracking()
		print(maze)

		pygame.display.flip()
		clock.tick(600)

def RecursiveBacktracking():
	direction_possible = [False, False, False, False]
	CheckAdjacent(direction_possible)

	go = False
	while go == False:	#find en bedre måde at gøre det her på...
		random_value = randint(0, 3)
		if direction_possible[random_value] == True:
			go = True

	MoveRandom(random_value)


def CheckAdjacent(direction_possible):
	e = "Not a possible move"
	try:
		if current.y - 2 >= 0 and maze[current.x][current.y-2] == 0: #north
			direction_possible[0] = True
	except:
		print(e)

	try:
		if current.y + 2 <= maze_height and maze[current.x][current.y+2] == 0: #south
			direction_possible[1] = True
	except:
		print(e)

	try:
		if current.x + 2 <= maze_width and maze[current.x+2][current.y] == 0: #east
			direction_possible[2] = True
	except:
		print(e)

	try:
		if current.x - 2 >= 0 and maze[current.x-2][current.y] == 0: #west
			direction_possible[3] = True
	except:
		print(e)

	if True not in direction_possible:
		sys.exit()
		#Backtrack()
	if True in direction_possible:
		return direction_possible

def Backtrack():
	e = "No possible backtrack"
	n = 2
	try:
		if maze[current.x][current.y-n] == 1:
			current.y -= n
			RecursiveBacktracking()
		elif maze[current.x][current.y+n] == 1:
			current.y += n
			RecursiveBacktracking()
		elif maze[current.x+n][current.y] == 1:
			current.x += n
			RecursiveBacktracking()
		elif maze[current.x-n][current.y] == 1:
			current.x -= n
			RecursiveBacktracking()
		else:
			print(maze)
			sys.exit()
	except:
		print(e)


def MoveRandom(random_value):
	if random_value == 0:
		for i in range(0, 1):
			current.y -= 1
			maze[current.x][current.y] = 1

		print("Moved North")
	elif random_value == 1:
		for i in range(0, 1):
			current.y += 1
			maze[current.x][current.y] = 1

		print("Moved South")
	elif random_value == 2:
		for i in range(0, 1):
			current.x += 1
			maze[current.x][current.y] = 1

		print("Moved East")
	elif random_value == 3:
		for i in range(0, ):
			current.x -= 1
			maze[current.x][current.y] = 1

		print("Moved West")

GameLoop()