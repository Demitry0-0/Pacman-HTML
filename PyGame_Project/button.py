from game import screen, terminate, FON, name
import pygame
import sqlite3
import os


class Button:
    def __init__(self):
        self.word = ["Играть", "Загрузить карту", "Рекорды", "Выйти"]
        self.flag = True
        self.draw()

    def draw(self):
        font = pygame.font.Font(None, 30)
        play = font.render(self.word[0], 1, (255, 204, 0))
        self.play = font.size(self.word[0])
        new_map = font.render(self.word[1], 1, (255, 204, 0))
        self.new_map = font.size(self.word[1])
        records = font.render(self.word[2], 1, (255, 204, 0))
        self.records = font.size(self.word[2])
        bye = font.render(self.word[3], 1, (255, 204, 0))
        self.bye = font.size(self.word[3])
        screen.blit(play, (30, 300))
        screen.blit(new_map, (30, 340))
        screen.blit(records, (30, 380))
        screen.blit(bye, (30, 420))

    def chunks(self, lst, chunk_size):
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

    def map(self):
        self.flag = False
        screen.fill((0, 0, 0))
        path = r'map'
        files = os.listdir(path)
        font = pygame.font.Font(None, 30)
        lst = self.chunks(files, 20)
        i = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    p = event.pos
                    if 10 <= p[0] <= font.size('назад')[0] + 10 and 30 <= p[1] <= font.size('назад')[1] + 30:
                        if i:
                            i -= 1
                        else:
                            self.flag = True
                            screen.fill((0, 0, 0)), screen.blit(FON, (0, 0))
                            return
                    elif 920 <= p[0] <= font.size('далее')[0] + 920 and 30 <= p[1] <= font.size('далее')[1] + 30:
                        if i + 1 < len(lst):
                            i += 1
                    for _ in range(len(lst[i])):
                        if 400 <= p[0] <= font.size(lst[i][_])[0] + 400 and \
                                30 * _ + 30 <= p[1] <= font.size(lst[i][_])[1] + 30 + 30 * _:
                            name, self.flag = 'map\\' + lst[i][_], True
                            screen.fill((0, 0, 0)), screen.blit(FON, (0, 0))
                            return
            self.render(lst[i])
            screen.blit(font.render('назад', 1, (255, 255, 255)), (10, 30))
            screen.blit(font.render('далее', 1, (255, 255, 255)), (920, 30))
            pygame.display.flip()

    def render(self, lst):
        screen.fill((0, 0, 0))
        for i in range(len(lst)):
            font = pygame.font.Font(None, 30)
            screen.blit(font.render(lst[i], 1, (255, 255, 255)), (400, 30 * i + 30))

    def update(self, pos, flag=False):
        font = pygame.font.Font(None, 30)
        x, y = pos
        if 20 <= x <= 30 + self.play[0] + 10 and 300 <= y <= 300 + self.play[1] and self.flag:
            screen.blit(font.render(self.word[0], 1, (0, 0, 0)), (30, 300))
            if flag:
                return True
        elif 20 <= x <= 30 + self.new_map[0] + 10 and 340 <= y <= 340 + self.new_map[1] and self.flag:
            screen.blit(font.render(self.word[1], 1, (0, 0, 0)), (30, 340))
            if flag:
                self.map()
        elif 20 <= x <= 30 + self.records[0] + 10 and 380 <= y <= 380 + self.records[1] and self.flag:
            screen.blit(font.render(self.word[2], 1, (0, 0, 0)), (30, 380))
            if flag:
                self.score()
        elif 20 <= x <= 30 + self.bye[0] + 10 and 420 <= y <= 420 + self.bye[1] and self.flag:
            screen.blit(font.render(self.word[3], 1, (0, 0, 0)), (30, 420))
            if flag:
                terminate()
        elif self.flag:
            self.draw()

    def score(self):
        self.flag = False
        a = name[name.index('\\') + 1:]
        con = sqlite3.connect('data\\records.db')
        cur = con.cursor()
        result = cur.execute('''SELECT * from records where map="{}"'''.format(a)).fetchall()
        result = list(map(lambda x: x[1] + ' = ' + str(x[0]), sorted(result, key=lambda x: x[0])))[:10]
        self.render(result[::-1])
        font = pygame.font.Font(None, 30)
        screen.blit(font.render('назад', 1, (255, 255, 255)), (10, 30))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    p = event.pos
                    if 10 <= p[0] <= font.size('назад')[0] + 10 and 30 <= p[1] <= font.size('назад')[1] + 30:
                        self.flag = True
                        screen.fill((0, 0, 0)), screen.blit(FON, (0, 0))
                        return
