import pygame
import constants
from character import Character 

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

#create player

player = Character(100, 100)

# Main game loop
run = True
while run: 

    #draw player on screen
    player.draw(screen)

    #Event Handler

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()