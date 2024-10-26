import pygame
from random import randint
from game import mersz
from bomb import Bomb


class Merzopakostniy(pygame.sprite.Sprite):
    def __init__(self, group, pos, board, player):
        super().__init__(group)
        self.group = group
        self.image = mersz
        self.board = board
        self.player = player
        pos_x, pos_y = pos
        self.x = self.y = 0
        self.chek_lst = []
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.time = self.step = 0
        self.list_bomb = []

    def resize(self, size):
        self.image = pygame.transform.scale(self.image, (size, size))

    def move(self):
        b = self.board
        self.step += 1
        i, ln = 0, len(self.chek_lst)
        while i < ln and ln:
            self.chek_lst[i] -= 1
            if not self.chek_lst[i]:
                self.list_bomb[i].die()
                del self.list_bomb[i], self.chek_lst[i]
                ln = len(self.chek_lst)
            i += 1
        if self.step == 240:
            bx, by = b.get_coords((b.get_cell((self.rect.x, self.rect.y))))
            bomb = Bomb(self.group, bx, by)
            bomb.resize(30)
            self.list_bomb.append(bomb)
            self.chek_lst.append(randint(300, 390))
            self.step = 0
        if not self.y and not self.x:
            while True:
                self.y = randint(1, (len(self.board.wall_map) - 3))
                self.x = randint(1, (len(self.board.wall_map[0]) - 3))
                if not self.board.wall_map[self.y][self.x]:
                    self.x, self.y = self.board.get_coords((self.x, self.y))
                    break
        ls = (self.rect.x, self.rect.y)
        if self.y == self.rect.y and self.rect.x == self.x:
            self.x = self.y = 0
        elif self.y == self.rect.y:
            if self.x > self.rect.x:
                if 'black' == b.get_color(b.get_cell((ls[0] + 30, ls[1]))):
                    self.rect = self.rect.move(1, 0)
                else:
                    self.x = self.rect.x
            elif self.x < self.rect.x:
                if 'black' == b.get_color(b.get_cell((ls[0] - 1, ls[1]))):
                    self.rect = self.rect.move(-1, 0)
                else:
                    self.x = self.rect.x
        else:
            if self.y > self.rect.y:
                if 'black' == b.get_color(b.get_cell((ls[0], ls[1] + 30))):
                    self.rect = self.rect.move(0, 1)
                else:
                    self.y = self.rect.y
            elif self.y < self.rect.y:
                if 'black' == b.get_color(b.get_cell((ls[0], ls[1] - 1))):
                    self.rect = self.rect.move(0, -1)
                else:
                    self.y = self.rect.y

    def num_bomb(self):
        return self.list_bomb
