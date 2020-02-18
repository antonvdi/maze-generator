#cd C:\Users\Anton\Documents\GitHub\pro_eks
#cd C:\Users\Mathias Laptop\Documents\GitHub\pro_eks

import pygame

pygame.init()

width = int(input("Width?\n"))
height = int(input("Height?\n"))

if width < 50:
	width = 50
elif width > 3000:
	width = 3000
if height < 50:
	height = 50
elif height > 3000:
	height = 3000


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