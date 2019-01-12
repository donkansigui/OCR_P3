# coding: utf-8
# pylint: disable=no-member
""" creation of the maze """
import random
from pygame.constants import (
    K_RIGHT, K_LEFT, K_UP, K_DOWN
)
from parse import *
from mcgyver import *
from murdock import *
from object import *


class Maze:
    """ creation of the maze """
    def __init__(self):
        """ positioning elements of the maze """
        self.map = call_parse()
        self.McGyver = McGyver(13, 13)
        self.Murdock = Murdock(1, 1)
        self.lst_obj = []
        self.append_Obj()
        print self.lst_obj

    def append_Obj(self):
        """ positioning inventory objects """
        obj = self.random_position()
        needle = Object(obj[0][0], obj[0][1])
        ether = Object(obj[1][0], obj[1][1])
        plastic_tube = Object(obj[2][0], obj[2][1])
        self.lst_obj.append(needle)
        self.lst_obj.append(ether)
        self.lst_obj.append(plastic_tube)

    def random_position(self):
        """ positioning of walls and empty spaces """
        i = 0
        self.wall = []
        self.wall_lst = []
        self.empty_lst = []
        for line in self.map:
            j = 0
            for square in line:
                position = (j*40, i*40)
                position_tab = [j, i]
                if square == "x":
                    self.wall_lst.append(position)
                elif square == " ":
                    self.empty_lst.append(position_tab)
                j = j+1
            i = i+1
        for data in self.empty_lst:
            if data[0] == 3 and data[1] == 3:
                print "error"
        self.empty_lst.remove([1, 13])

        return random.sample(self.empty_lst, 3)

    def check_destination(self, map, event):
        """ verification of the destination
            for the movements of the character
        """
        if event.key == K_DOWN and map[self.x+1][self.y]:
            self.x = self.x + 1
        if event.key == K_UP and map[self.x-1][self.y]:
            self.x = self.x - 1
        if event.key == K_LEFT and map[self.x][self.y-1]:
            self.y = self.y - 1
        if event.key == K_RIGHT and map[self.x][self.y+1]:
            self.y = self.y + 1

    def check_destination(self, map):
        """ verification of the destination
            for the movements of the character
        """
        if event.key == K_DOWN and map[self.McGyver.x+1][self.McGyver.y]:
            self.McGyver.x = self.McGyver.x + 1
        if event.key == K_UP and map[self.McGyver.x-1][self.McGyver.y]:
            self.McGyver.x = self.McGyver.x - 1
        if event.key == K_LEFT and map[self.McGyver.x][self.McGyver.y-1]:
            self.McGyver.y = self.McGyver.y - 1
        if event.key == K_RIGHT and map[self.McGyver.x][self.McGyver.y+1]:
            self.McGyver.y = self.McGyver.y + 1

            position_perso = position_perso.move(0, 40)
            mcx = mcx+1
