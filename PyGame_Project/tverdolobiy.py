import pygame
from game import lob_img


class Tverdolobiy(pygame.sprite.Sprite):
    def __init__(self, group, pos, board, player):
        super().__init__(group)
        self.image = lob_img
        pos_x, pos_y = pos
        self.board = board
        self.player = player
        self.speed = 0.1
        self.chek_lst = []
        self.wall = []
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def resize(self, size):
        self.image = pygame.transform.scale(self.image, (size, size))

    def payment(self, player, lob):
        n = 200
        if abs(player[0] - lob[0]) > n or abs(player[1] - lob[1]) > 150:
            return True
        return False

    def move(self):
        board, player = self.board, self.player
        lob_cell = (self.rect.x, self.rect.y)
        player_cell = (int(player.x), int(player.y))
        if not len(self.chek_lst) and self.payment(player_cell, lob_cell):
            self.chek_lst.append(player_cell)
        elif len(self.chek_lst) and self.payment(player_cell, self.chek_lst[-1]):
            self.chek_lst.append(player_cell)
        if len(self.chek_lst):
            if self.chek_lst[0][0] > lob_cell[0]:
                self.rect = self.rect.move(1, 0)
            elif self.chek_lst[0][0] < lob_cell[0]:
                self.rect = self.rect.move(-1, 0)
            elif self.chek_lst[0][1] > lob_cell[1]:
                self.rect = self.rect.move(0, 1)
            elif self.chek_lst[0][1] < lob_cell[1]:
                self.rect = self.rect.move(0, -1)
            self.rect = self.rect.move(0, 0)
            if self.chek_lst[0] == lob_cell:
                del self.chek_lst[0]
        ls = board.get_cell((self.rect.x, self.rect.y))
        if board.get_color(ls) == 'white':
            board.open_map(ls)
            self.wall.append(ls)
            self.board.board[ls[0]][ls[1]].color = 'black'
        elif len(self.wall) and ls != self.wall[0]:
            board.open_map(self.wall[0])
            self.board.board[self.wall[0][0]][self.wall[0][1]].color = 'white'
            del self.wall[0]

    def die(self):
        self.kill()
