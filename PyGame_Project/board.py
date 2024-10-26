from cell import Cell
from game import screen
import time
import pygame


class Board:
    # создание поля
    def __init__(self, width, height, wall_map=[[1, 1, 1, 1, 1],
                                                [1, 0, 0, 0, 1],
                                                [1, 0, 1, 0, 1],
                                                [1, 0, 0, 0, 1],
                                                [1, 0, 1, 0, 1],
                                                [1, 0, 0, 0, 1],
                                                [1, 1, 1, 1, 1]]):
        self.width = width
        self.count = 0
        self.height = height
        self.wall_map = wall_map
        self.board = []
        self.hero = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.check_points = {None}
        self.cells = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.fill_cells()
        self.create_cells()

    def create_cells(self):
        for i in range(self.height):
            self.board.append([])
            for j in range(self.width):
                if self.wall_map[j][i] == '0':
                    self.wall_map[j][i] = 0
                    self.board[i].append(Cell(i, j))
                elif self.wall_map[j][i] == '1':
                    self.wall_map[j][i] = 1
                    self.board[i].append(Cell(i, j, color='white'))
                elif self.wall_map[j][i] == '@':
                    self.hero[0] = (i * 30 + 30, j * 30 + 30)
                    self.wall_map[j][i] = 0
                    self.board[i].append(Cell(i, j))
                elif self.wall_map[j][i] == '#':
                    self.hero[1] = (i * 30 + 30, j * 30 + 30)
                    self.wall_map[j][i] = 0
                    self.board[i].append(Cell(i, j))
                elif self.wall_map[j][i] == '*':
                    self.hero[2] = (i * 30 + 30, j * 30 + 30)
                    self.wall_map[j][i] = 0
                    self.board[i].append(Cell(i, j))
                elif self.wall_map[j][i] == '$':
                    self.hero[3] = (i * 30 + 30, j * 30 + 30)
                    self.wall_map[j][i] = 0
                    self.board[i].append(Cell(i, j))

    def are_left(self):
        checked = True
        for rd in self.board:
            for cell in rd:
                if cell.collectable and not cell.collected:
                    checked = False
                    break
        return not checked

    def reset(self):
        for rd in self.board:
            for cell in rd:
                if cell.collectable:
                    cell.collected = False
                    time.sleep(0.1)
                    self.render()
                    pygame.display.flip()
                else:
                    time.sleep(0.1)
        self.count += len(self.check_points) - 1
        self.check_points.clear()

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.fill_cells()

    def render(self):
        for i in range(self.height - 1):
            for j in range(self.width - 1):
                self.board[i][j].draw(self.top + i * self.cell_size,
                                      self.left + j * self.cell_size, self.cell_size,
                                      self.cell_size)
                if not len(self.check_points):
                    self.board[i][j].check = None
                else:
                    self.check_points.add(self.board[i][j].check)
                if self.board[i][j].color == "white" and False:
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.top + i * self.cell_size,
                        self.left + j * self.cell_size, self.cell_size,
                        self.cell_size))
                if self.board[i][j].color == "black" and False:
                    pygame.draw.rect(screen, (0, 0, 0), (
                        self.top + i * self.cell_size,
                        self.left + j * self.cell_size, self.cell_size,
                        self.cell_size))

    def fill_cells(self):
        for i in range(self.height):
            for j in range(self.width):
                self.cells[i][j] = [self.top + i * self.cell_size,
                                    self.left + j * self.cell_size,
                                    self.cell_size,
                                    self.cell_size]

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)

    def on_click(self, cell):
        return

    def load_map(self, file_adr):
        with open(file_adr, 'r') as f:
            _map = list(f.read().split('\n'))
            wall_map = [x.split() for x in _map]
            x = len(wall_map)
            y = len(wall_map[0])
        a = Board(x, y, wall_map)
        a.wall_map = wall_map
        return a

    def get_cell(self, pos):
        pos = int(pos[0] + 0), int(pos[1] + 0)
        i, j = -1, -1
        for cell_row in self.cells:
            i += 1
            if cell_row[0][0] <= pos[0] < cell_row[0][0] + self.cell_size:
                for cell in cell_row:
                    j += 1
                    if cell[1] <= pos[1] < cell[1] + self.cell_size:
                        return [i, j]
        return [-1, -1]

    def get_coords(self, ij):
        return (30 * ij[0] + 30, 30 * ij[1] + 30)

    def change_color(self, i):
        if self.board[i[0]][i[1]].color == "black":
            self.board[i[0]][i[1]].color = "white"
        elif self.board[i[0]][i[1]].color == "white":
            self.board[i[0]][i[1]].color = "black"

    def open_map(self, i):
        self.board[i[0]][i[1]].change_color()

    def get_color(self, i):
        return self.board[i[0]][i[1]].color
