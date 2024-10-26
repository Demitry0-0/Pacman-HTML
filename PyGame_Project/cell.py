from game import screen
import pygame


class Cell:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.check = None
        self.color = color
        self.collectable = True if color == "black" else False
        self.collected = False

    def change_color(self):
        if self.color == "white":
            self.color = "black"
        if self.color == "black":
            self.color = "white"

    def draw(self, *args):
        # args = (self.top + i * self.cell_size,
        # self.left + j * self.cell_size, self.cell_size,
        # self.cell_size)

        if self.color == "black" and self.collectable and self.collected:
            pygame.draw.rect(screen, (0, 0, 0), args)
            self.check = args[:2]
        elif self.color == "black" and self.collectable and not self.collected:
            # draw collectable sprite
            pygame.draw.rect(screen, (0, 0, 0), args)
            pygame.draw.circle(screen, (255, 255, 255), (args[0] + args[2] // 2, args[1] + args[2] // 2), args[2] // 6)
        elif self.color == "white" and not self.collectable:
            pygame.draw.rect(screen, (200, 200, 255), args)
