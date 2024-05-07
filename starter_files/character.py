import pygame
import math
import constants
class Character():
    def __init__(self, x, y, animation_list):
        self.flip = False
        self.image = animation_list[0]
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def mvoe(self, dx, dy):

        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False
        #control diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)


        self.rect.x += dx
        self.rect.y += dy


    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, constants.RED, self.rect, 1)