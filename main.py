import pygame

pygame.init()

clock = pygame.time.Clock()

crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		print(event)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()