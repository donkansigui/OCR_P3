# coding: utf-8
# pylint: disable=no-member
""" creation of the maze """
import random
import pygame
from parse import call_parse
from mcgyver import McGyver
from murdock import Murdock
from object import Object


class Maze(object):
    """ creation of the maze """
    def __init__(self):
        """ positioning elements of the maze """
        self.wall = []
        self.wall_lst = []
        self.empty_lst = []
        self.map = call_parse()
        self.mc_gyver = McGyver(13, 13)
        self.murdock = Murdock(1, 1)
        self.lst_obj = []
        self.append_obj()
        print (self.lst_obj)

    def append_obj(self):
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
                print ("error")
        self.empty_lst.remove([1, 13])

        return random.sample(self.empty_lst, 3)
