import pygame
import constants

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

# Main game loop
run = True
while run: 

    #Event Handler

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()