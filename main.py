# cd C:\Users\Anton\Documents\GitHub\pro_eks
# cd C:\Users\anton_mc03yx6\Documents\GitHub\pro_eks
# cd C:\Users\Mathias Laptop\Documents\GitHub\pro_eks

import pygame
import sys, time, os
from random import randint
import random

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,25)
pygame.init()

maze_width = 0
maze_height = 0
tile_size = 0

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((500, 500))

maze = [[]] #generer bitmap
path = []

x_start = 1
y_start = 1

class current(object):  
    x = x_start
    y = y_start
    def __init__(self, x, y):
    	self.x = x
    	self.y = y

def Main():
	done = False
	generatemaze = input("Type 'generate'")

	screen.fill(black) #resetter skærmen

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		if generatemaze == "generate":
			generatemaze = ""
			InitDisplay()
			GenerateMaze()

def GenerateMaze():
	start_time = time.time() #starter clock
	game_over = False

	while game_over == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		RecursiveBacktracking()
		pygame.display.flip()
		pygame.event.pump() #for at undgå timeout

		if len(path) == 0:
			print("runtime: " + str(time.time() - start_time))
			game_over = True

def InitDisplay():
	global maze 
	global maze_width
	global maze_height
	global tile_size

	maze_width = int(input("Maze width:\n"))
	maze_height = int(input("Maze height:\n"))
	tile_size = int(input("Maze tile size\n"))

	if maze_width % 2 == 0:
		maze_width += 1
	if maze_height % 2 == 0:
		maze_height += 1

	screen = pygame.display.set_mode((maze_width * tile_size, maze_height * tile_size))
	
	maze = [[0 for i in range(maze_height)] for j in range(maze_width)] #generer bitmap
	maze[current.x][current.y] = 1
	maze[1][0] = 2
	maze[maze_width-2][maze_height-1] = 2 #indstiller start og slut for maze

	for i in range(maze_width): # tegner mazen som den ser ud til at begynde med
		for j in range(maze_height):
			if maze[i][j] == 1:
				pygame.draw.rect(screen, white, [i*tile_size, j*tile_size, tile_size, tile_size])

			if maze[i][j] == 2:
				pygame.draw.rect(screen, red, [i*tile_size, j*tile_size, tile_size, tile_size])

def RecursiveBacktracking():
	backwards = False

	direction_possible = [False, False, False, False]

	CheckAdjacent(direction_possible)

	if True not in direction_possible:
		backwards = True
		Backtrace(direction_possible)
			
	go = False
	while go == False:
		random_value = randint(0, 3)
		if direction_possible[random_value] == True:
			if backwards == False:
				path.append(random_value)
			go = True

	MoveRandom(random_value)

def CheckAdjacent(direction_possible):
	try:
		if current.y-2 >= 0 and maze[current.x][current.y-2] == 0: #north
			direction_possible[0] = True
	except IndexError:
		pass

	try:
		if current.y+2 <= maze_height and maze[current.x][current.y+2] == 0: #south
			direction_possible[1] = True
	except IndexError:
		pass

	try:
		if current.x+2 <= maze_width and maze[current.x+2][current.y] == 0: #east
			direction_possible[2] = True
	except IndexError:
		pass

	try:
		if current.x-2 >= 0 and maze[current.x-2][current.y] == 0: #west
			direction_possible[3] = True
	except IndexError:
		pass

	return direction_possible 

def Backtrace(direction_possible):
	if path[-1] == 0:
		direction_possible[1] = True
	elif path[-1] == 1:
		direction_possible[0] = True
	elif path[-1] == 2:
		direction_possible[3] = True
	elif path[-1] == 3:
		direction_possible[2] = True
	del path[-1]
	return direction_possible

def MoveRandom(random_value):
	if random_value == 0:
		for i in range(2):
			current.y -= 1
			maze[current.x][current.y] = 1
			pygame.draw.rect(screen, white, [current.x*tile_size, current.y*tile_size, tile_size, tile_size])
	elif random_value == 1:
		for i in range(2):
			current.y += 1
			maze[current.x][current.y] = 1
			pygame.draw.rect(screen, white, [current.x*tile_size, current.y*tile_size, tile_size, tile_size])
	elif random_value == 2:
		for i in range(2):
			current.x += 1
			maze[current.x][current.y] = 1
			pygame.draw.rect(screen, white, [current.x*tile_size, current.y*tile_size, tile_size, tile_size])
	elif random_value == 3:
		for i in range(2):
			current.x -= 1
			maze[current.x][current.y] = 1
			pygame.draw.rect(screen, white, [current.x*tile_size, current.y*tile_size, tile_size, tile_size])

Main()