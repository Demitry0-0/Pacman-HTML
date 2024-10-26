from game import bb
import pygame


class Bomb(pygame.sprite.Sprite):
    def __init__(self, group, pos_x, pos_y):
        super().__init__(group)
        self.image = bb
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def resize(self, size):
        self.image = pygame.transform.scale(self.image, (size, size))

    def die(self):
        self.kill()
