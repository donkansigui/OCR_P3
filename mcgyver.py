# coding: utf-8
""" assigning values ​​for character positioning """


class McGyver(object):
    """ assigning values ​​for character positioning """
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.lst_obj = [False, False, False]

    def move(self, x_position, y_position):
        """ assigning values ​​for character positioning """
        self.x_position += x_position
        self.y_position += y_position
