# cd C:\Users\Anton\Documents\GitHub\pro_eks
# cd C:\Users\anton_mc03yx6\Documents\GitHub\pro_eks
# cd C:\Users\Mathias Laptop\Documents\GitHub\pro_eks

import pygame
import time, os
from random import randint

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,25) #start position for vinduet
pygame.init()
pygame.font.init() #initialiserer pygame og pygame font
title_font = pygame.font.Font("freesansbold.ttf", 50) #vælger title font
font = pygame.font.Font("freesansbold.ttf", 24) #vælger font

maze_width = 3
maze_height = 3
tile_size = 1 #startværdier for variable

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0) #definerer farver

screen = pygame.display.set_mode((700, 700)) #definerer screen skærmen

maze = [[]] #definerer bitmap
path = [] #definerer en tom liste, der indeholder vejen som programmet har bevæget

class current(object):  
    x = 1
    y = 1
    def __init__(self, x, y):
    	self.x = x
    	self.y = y #når der initialiseres, indstilles current objektet til (1, 1)

def Main():
	global maze_width
	global maze_height
	done = False
	mpos = (0,0)

	title = DrawText("Generate Maze and Export as Image", 30)
	title1 = DrawText("Generate and Solve with DFS", 90)
	maze_size = DrawText(str(maze_width) + "x" + str(maze_height), 600)
	maze_width_increase = DrawText("+1 width", 550)
	maze_height_increase = DrawText("+1 height", 650)
	
	while not done: #når programmet ikke er færdigt...
		for event in pygame.event.get(): #eventhandling
			if event.type == pygame.QUIT: #hvis der trykkes x er programmet færdigt
				done = True
			if event.type == pygame.MOUSEBUTTONUP: #hvis der trykkes på musen, skal mpos() opdateres
				mpos = pygame.mouse.get_pos()

		if title.collidepoint(mpos): #hvis title-teksten kolliderer med mpos(), så generer og eksporter et maze
			InitDisplay()
			GenerateMaze()
			pygame.image.save(screen, "mazes/maze.png")
			mpos = (0, 0) #reset mpos
		if maze_width_increase.collidepoint(mpos): #hvis der trykkes +1 maze width, så forøg maze width, opdater tekst og opdater mpos
			maze_width += 1
			mpos = (0, 0)
			maze_size = DrawText(str(maze_width) + "x" + str(maze_height), 600)
		if maze_height_increase.collidepoint(mpos):
			maze_height += 1
			mpos = (0, 0)
			maze_size = DrawText(str(maze_width) + "x" + str(maze_height), 600)
			
		pygame.display.update() 
		pygame.event.pump() #for at undgå timeout

def DrawText(text, offset_y):
	title = font.render(text, True, (255, 255, 255))
	titleRect = title.get_rect()
	titleRect.centerx = screen.get_rect().centerx
	titleRect.centery = offset_y
	screen.blit(title, titleRect)

	return titleRect

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
	pygame.event.pump()
	maze_height = int(input("Maze height:\n"))
	pygame.event.pump()
	tile_size = int(input("Maze tile size\n"))
	pygame.event.pump()

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