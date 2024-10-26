import random
import pygame


class Player:
    def __init__(self, screen, anime, board, pos):
        self.anime = anime
        self.screen = screen
        self.board = board
        self.x, self.y = pos
        self.dir = 'down'
        self.new_dir = '_'
        self.speed = 0.7
        self.board_pos = self.get_board_pos()
        self.spos = self.board_pos

    def reverse_dir(self):
        if self.dir == 'up':
            return 'down'
        if self.dir == 'down':
            return 'up'
        if self.dir == 'left':
            return 'right'
        if self.dir == 'right':
            return 'left'

    def set_dir(self, dir):
        self.new_dir = dir

    def check_change(self):
        if self.board_pos != self.get_board_pos():
            self.board_pos = self.get_board_pos()
            self.x, self.y = self.get_board_pos(5, 5)[0] * self.board.cell_size + self.board.left, \
                             self.get_board_pos(5, 5)[1] * self.board.cell_size + self.board.top
            self.spos = self.get_board_pos(5, 5)
            if self.board.board[self.spos[0]][self.spos[1]].collectable:
                self.board.board[self.spos[0]][self.spos[1]].collected = True
            return True
        return False

    def get_board_pos(self, offsetx=0, offsety=0):
        return self.board.get_cell((self.x + offsetx, self.y + offsety))

    def get_possibles(self):
        a = []
        if self.board.wall_map[self.spos[1] + 1][self.spos[0]] == 0:
            a.append('down')
        if self.board.wall_map[self.spos[1] - 1][self.spos[0]] == 0:
            a.append('up')
        if self.board.wall_map[self.spos[1]][self.spos[0] - 1] == 0:
            a.append('left')
        if self.board.wall_map[self.spos[1]][self.spos[0] + 1] == 0:
            a.append('right')
        return a  # ['up', 'down', 'right', 'left']

    def move(self, possibles):
        if self.check_change():
            possibles = self.get_possibles()
            if self.dir not in possibles:
                self.dir = random.choice(possibles)
                self.anime.rotate(self.dir)
            if self.new_dir in possibles:
                self.dir = self.new_dir
                self.anime.rotate(self.dir)
        self.anime.dir = self.dir
        if self.dir == 'up':
            self.y -= self.speed
        if self.dir == 'down':
            self.y += self.speed
        if self.dir == 'left':
            self.x -= self.speed
        if self.dir == 'right':
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, (200, 200, 10), (self.x, self.y, self.board.cell_size, self.board.cell_size))
