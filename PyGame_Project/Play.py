import pygame
from player import Player
from board import Board
from anime import Anime
from tverdolobiy import Tverdolobiy
from merzopakostniy import Merzopakostniy
from legushka import Legushka
from button import Button
from chek import Check
from finish import Finish
from game import screen, terminate, FPS, FON, draw, name

up, down, left, right = ([119, 275], [115, 273], [97, 274], [100, 276])
clock = pygame.time.Clock()


def game():
    group = pygame.sprite.Group()
    player_anim = Anime(group, (228, 288))
    board = Board.load_map(None, name)
    board.set_view(30, 30, 30)
    lst = []
    if sum(board.hero[0]):
        player = Player(screen, player_anim, board, board.hero[0])
        player_anim.resize(30)
    if sum(board.hero[1]):
        tverdolobiy = Tverdolobiy(group, board.hero[1], board, player)
        tverdolobiy.resize(30)
        lst.append(tverdolobiy)
    if sum(board.hero[2]):
        merzopakostniy = Merzopakostniy(group, board.hero[2], board, player)
        merzopakostniy.resize(30)
    if sum(board.hero[3]):
        legushka = Legushka(group, board.hero[3], board, player)
        legushka.resize(30)
        lst.append(legushka)
    running = True
    c = 0
    while running:
        c += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key in up:
                    player.set_dir('up')
                if event.key in down:
                    player.set_dir('down')
                if event.key in left:
                    player.set_dir('left')
                if event.key in right:
                    player.set_dir('right')
                if event.key == pygame.K_LEFT:
                    player.set_dir('left')
                if event.key == pygame.K_RIGHT:
                    player.set_dir('right')
                if event.key == pygame.K_UP:
                    player.set_dir('up')
                if event.key == pygame.K_DOWN:
                    player.set_dir('down')
        screen.fill((0, 0, 0))
        board.render()
        if not len(board.check_points):
            board.check_points.add(None)
        if not board.are_left():
            board.reset()
        player.move([])
        player_anim.rect.x, player_anim.rect.y = player.x, player.y
        if sum(board.hero[2]):
            merzopakostniy.move()
        if not c % 2:
            if sum(board.hero[3]):
                legushka.move()
            if sum(board.hero[1]):
                tverdolobiy.move()
        group.draw(screen)
        if c % 20 == 0:
            player_anim.update()
        if sum(board.hero[2]):
            check = Check(player, merzopakostniy.num_bomb() + lst)
        elif sum(board.hero[0]):
            check = Check(player, lst)
        if check.checkaed():
            running = False
        draw(str(len(board.check_points) - 1 + board.count))
        pygame.display.flip()
        clock.tick(FPS*2)
    Finish(group, str(len(board.check_points) - 1 + board.count))


def load_screen():
    if True:
        p = (-1, -1)
        f = False
        group = pygame.sprite.Group()
        b = Button()
        screen.blit(FON, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEMOTION:
                    p = event.pos
                    group.update(event.pos, False)
                    b.update(event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if b.update(event.pos, True):
                        game()
                        return
            group.update(p, f)
            group.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)


while True:
    load_screen()