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
        #take keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("left")
            if event.key == pygame.K_d:
                print("right")
            if event.key == pygame.K_w:
                print("up")
            if event.key == pygame.K_s:
                print("down")
                

            
        
    pygame.display.update()

pygame.quit()