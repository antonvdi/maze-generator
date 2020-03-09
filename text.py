import pygame

def text_to_screen(screen, text, x, y, size = 50,
        color = (255, 255, 255), font_type = 'Trebuchet MS'):
        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))