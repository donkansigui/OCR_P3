# coding: utf-8


class McGyver:
    """ assigning values ​​for character positioning """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lstObj = [False, False, False]

    def move(self, x, y):
        self.x += x
        self.y += y
