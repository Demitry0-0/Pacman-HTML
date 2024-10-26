class Check:
    def __init__(self, player, lst):
        self.lst = lst
        self.player = player

    def checkaed(self):
        x, y = int(self.player.x), int(self.player.y)
        x, y = set(range(x, x + 30)), set(range(y, y + 30))
        for name in self.lst:
            name_x = set(range(name.rect.x + 7, name.rect.x + 23))
            name_y = set(range(name.rect.y + 7, name.rect.y + 23))
            if name_x & x and name_y & y:
                return True
