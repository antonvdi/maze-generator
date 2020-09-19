import pygame
import time, os
from random import randint

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,25) #start position for vinduet
pygame.init()

maze_width = int(input("Maze width:\n"))
maze_height = int(input("Maze height:\n"))
tile_size = int(input("Maze tile size\n"))

if maze_width % 2 == 0:
	maze_width += 1
if maze_height % 2 == 0:
	maze_height += 1

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
	done = False
	generated = False

	while not done: #når programmet ikke er færdigt...
		for event in pygame.event.get(): #event-handling
			if event.type == pygame.QUIT: #hvis der trykkes 'x' er programmet færdigt
				done = True

			if generated == False:
				InitDisplay() #klargører display og genererer tomt bitmap i rigtig størrelse
				GenerateMaze() #generer hele mazen
				pygame.image.save(screen, "mazes/maze.png") #gemmer mazen som en png fil i en under mappe, der hvor filen er placeret
				generated = True
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
					generated = False

def InitDisplay():
	global maze 
	global maze_width
	global maze_height
	global tile_size

	screen = pygame.display.set_mode((maze_width * tile_size, maze_height * tile_size))
	
	maze = [[0 for i in range(maze_height)] for j in range(maze_width)] #generer bitmap
	maze[current.x][current.y] = 1 
	maze[1][0] = 2 #indstiller start og slut for maze
	maze[maze_width-2][maze_height-1] = 2 

	for i in range(maze_width): # tegner mazen som den ser ud til at begynde med
		for j in range(maze_height):
			if maze[i][j] == 1:
				pygame.draw.rect(screen, white, [i*tile_size, j*tile_size, tile_size, tile_size])

			if maze[i][j] == 2:
				pygame.draw.rect(screen, red, [i*tile_size, j*tile_size, tile_size, tile_size])

def GenerateMaze():
	start_time = time.time() #starter clock
	game_over = False

	while game_over == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		NextStep()
		pygame.display.flip()
		pygame.event.pump() #for at undgå timeout

		if len(path) == 0: #tjek om programmet er færdig med at generere
			print("Runtime: " + str(time.time() - start_time))
			print("Finished. Press 'R' to run again")
			game_over = True

def NextStep():
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
	try: #hvis der kommer en index error, kan current positionen ikke bevæge sig i den pågældende retning. derfor fortsætter den med næste check
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
	#path listen indeholder alle de retninger current har bevæget sig. index '-1' er den sidste position i listen.
	# 0 = nord, 1 = syd, 2 = øst, 3 = vest. 
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
