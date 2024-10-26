import pygame
import os
import sys

FPS = 60
size = WIDTH, HEIGHT = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
name = 'map\\map1.html'
pygame.init()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey == 2:
        image = pygame.image.load(fullname).convert()
    return image


mersz = load_image('mersz.jpg')
bb = load_image('bomb.jpg')
leg_img = load_image('leg.png')
lob_img = load_image('lob.png', None)
FON = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))


def draw(txt):
    if 6 - len(txt) < 0:
        txt = '999999'
    else:
        txt = (6 - len(txt)) * '0' + txt
    font = pygame.font.Font(None, 30)
    text = font.render("hight score " + txt, 1, (100, 255, 100))
    screen.blit(text, (30, 0))

