import pygame
from game import load_image, terminate, screen, name
import time
import sqlite3


class Finish(pygame.sprite.Sprite):
    def __init__(self, group, record):
        super().__init__(group)
        self.image = load_image('die.jpg')
        self.rect = self.image.get_rect().move(-1000, 0)
        pygame.mixer.music.load('data\\probitie.wav')
        pygame.mixer.music.play()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN and not self.rect.x:
                    x, y = event.pos
                    if 20 <= x <= 230 and 320 <= y <= 350:
                        return
                    elif 20 <= x <= 195 and 455 <= y <= 485:
                        a = name[name.index('\\') + 1:]
                        con = sqlite3.connect('data\\records.db')
                        cur = con.cursor()
                        hero = input('Введите ник: ')
                        result = cur.execute('''SELECT * from records where map="{}" 
                        AND name="{}"'''.format(a, hero)).fetchall()
                        if len(result):
                            if result[0][0] < int(record):
                                cur.execute('''UPDATE records SET point = {}
                                 WHERE name = "{}"'''.format(int(record), hero)).fetchall()
                        else:
                            cur.execute('''INSERT INTO records 
                            VALUES ({},"{}","{}")'''.format(int(record), hero, a)).fetchall()
                            con.commit()
                        print('Успешно введино')
                    elif 20 <= x <= 125 and 545 <= y <= 575:
                        terminate()
            if self.rect.x < 0:
                self.rect.x += 2
            time.sleep(0.00001)
            group.draw(screen)
            group.update()
            pygame.display.flip()
