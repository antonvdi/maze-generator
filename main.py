#cd C:\Users\Anton\Documents\GitHub\pro_eks
#cd C:\Users\Mathias Laptop\Documents\GitHub\pro_eks

import pygame

pygame.init()

width = 800
height = 800

maze = []

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

maze = [[0 for i in range(int(width/10))] for j in range(int(height/10))]
			
print(maze)

def GameLoop():
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		x = 0
		y = 0
		#RecursiveBacktracking(x, y)

		pygame.display.flip()
		clock.tick(60)

#def RecursiveBacktracking(x, y):
	

	


GameLoop()