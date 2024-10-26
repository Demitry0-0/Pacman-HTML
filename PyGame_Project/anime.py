from game import load_image
import pygame


class Anime(pygame.sprite.Sprite):
    kadrs = [load_image('packman_1.png'),
             load_image('packman_2.png'),
             load_image('packman_3.png'),
             load_image('packman_4.png')]

    def __init__(self, group, pos):
        super().__init__(group)
        self.index = 0
        self.angle = 0
        self.image = pygame.transform.rotate(Anime.kadrs[0], self.angle)
        self.cimage = self.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = 'down'

    def update(self):
        a = [0, 1, 2, 3, 2, 1]
        self.index += 1
        self.index %= 6
        self.cimage = Anime.kadrs[a[self.index]]
        self.rotate(self.dir)

    def resize(self, size):
        for i in range(len(Anime.kadrs)):
            Anime.kadrs[i] = pygame.transform.scale(Anime.kadrs[i], (size, size))

    def rotate(self, dir):
        if dir == 'up':
            self.angle = 90
        if dir == 'down':
            self.angle = -90
        if dir == 'left':
            self.angle = -180
        if dir == 'right':
            self.angle = 0
        self.image = pygame.transform.rotate(self.cimage, self.angle)
