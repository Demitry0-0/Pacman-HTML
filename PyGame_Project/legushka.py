import pygame
from game import leg_img


class Legushka(pygame.sprite.Sprite):
    def __init__(self, group, pos, board, player):
        super().__init__(group)
        pos_x, pos_y = pos
        self.image = leg_img
        self.board = board
        self.player = player
        self.speed = 0.5
        self.x = self.y = 0
        self.chek_lst = []
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def resize(self, size):
        self.image = pygame.transform.scale(self.image, (size, size))

    def payment(self, leg_cell):
        lst = [self.chek_lst[0], leg_cell]
        count = 1
        x = (lst[0][0] - lst[1][0])
        y = (lst[0][1] - lst[1][1])
        while True:
            if 0 != abs(x / (count + 1)) < 1 or 0 != abs(y / (count + 1)) < 1:
                x, y = x / count, y / count
                break
            count += 1
        if not int(x) and not int(y):
            y = x = 1
        return (x, y)

    def move(self):
        x, y = self.x, self.y
        board, player = self.board, self.player
        leg_cell = (self.rect.x, self.rect.y)
        player_cell = (int(player.x), int(player.y))
        if not len(self.chek_lst) and board.get_color(board.get_cell(player_cell)) \
                and player_cell[0] % 30 == 0 and player_cell[1] % 30 == 0:
            self.chek_lst.append(player_cell)
            self.x, self.y = x, y = self.payment(leg_cell)
        elif len(self.chek_lst) and (leg_cell[0], leg_cell[1]) == self.chek_lst[0]:
            if abs(leg_cell[0] - player_cell[0]) >= 150 or \
                    abs(leg_cell[1] - player_cell[1]) >= 150:
                del self.chek_lst[0]
            else:
                x = y = 0
        if len(self.chek_lst):
            if leg_cell[0] == self.chek_lst[0][0]:
                self.rect = self.rect.move(0, y)
            elif leg_cell[1] == self.chek_lst[0][1]:
                self.rect = self.rect.move(x, 0)
            else:
                self.rect = self.rect.move(x, y)

    def die(self):
        self.kill()
