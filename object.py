# coding: utf-8
""" function used for positioning objects"""


class Object(object):
    """ assigning values ​​for positioning objects """
    def __init__(self, x, y):
        """ assigning values ​​for positioning objects """
        self.x_position = x
        self.y_position = y
        self.to_display = True

    def set_position(self, x_position, y_position):
        """ assigning values ​​for positioning objects """
        self.x_position = x_position
        self.y_position = y_position

    def toggle(self, to_display):
        """ assigning values ​​for positioning objects """
        self.to_display = to_display
