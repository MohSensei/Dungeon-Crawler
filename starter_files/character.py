import pygame
class Character():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)