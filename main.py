#cd C:\Users\Anton\Documents\GitHub\pro_eks

import pygame

pygame.init()

grid = []

width = 800
height = 800

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def GameLoop():
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		x = 0
		y = 0
		RecursiveBacktracking(x, y)

		pygame.display.flip()
		clock.tick(60)


def RecursiveBacktracking(x, y):


	


GameLoop()