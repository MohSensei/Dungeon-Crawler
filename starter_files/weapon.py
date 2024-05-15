import pygame
class Weapon():
    def __init__(self, image):
        self.original_image = image 
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()

    def update(self, player):
        self.rect.center = player.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)