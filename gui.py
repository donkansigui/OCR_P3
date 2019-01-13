#! /usr/bin/env python3
# coding: utf-8
# pylint: disable=no-member
""" setting up the game """

import sys
import pygame
from pygame.locals import *
from pygame.constants import (
    KEYDOWN, K_F1, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN
)
from pygame.draw import *
from maze import Maze as mz
from sprite import Sprite


# usefull game dimension
TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 15


class Gui:
    """ setting up the game """
    def __init__(self):
        """ setting up values """
        self.mcx = 13
        self.mcy = 13
        self.position_perso = [520, 520]
        self.maze = mz()
        self.pygame = pygame
        self.pygame.init()
        self.init_ui()
        self.pygame.font.init()
        self.myfont = self.pygame.font.SysFont('monospace', 16)
        self.Sprite = Sprite(self.pygame)

        self.rectangle = self.pygame.draw.rect(self.window_surface,
                                               (255, 255, 255), (0, 80, 0, 40))
        self.init_music()
        self.init_sprite()
        self.wall = pygame.image.load('./pictures/tile.png').convert()

    def init_music(self):
        """ setting up the music """
        self.pygame.mixer.music.load('./music/macgyver-theme-song.ogg')
        self.pygame.mixer.music.play(-1)
        self.pygame.mixer.music.set_volume(0.0)
        self.pygame.mixer.music.unpause()

    def init_ui(self):
        """ setting up the main window """
        self.window_surface = self.pygame.display.set_mode(
            (MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 40), 0, 32)
        self.pygame.display.set_caption('Mac Gyver')

    def init_sprite(self):
        """ setting up sprites positioning """
        self.position_perso = self.Sprite.index[1].get_rect(center=(540, 540))
        self.position_guard = self.Sprite.index[2].get_rect(center=(60, 60))
        self.position_rect = self.Sprite.index[4].get_rect(center=(320, 620))
        self.position_rect2 = self.Sprite.index[3].get_rect(center=(280, 620))
        self.position_rect3 =\
                            self.Sprite.index[5].get_rect(center=(240, 620))
        a_x = (self.maze.lst_obj[0].x_position)*40+20
        b_x = self.maze.lst_obj[0].y_position*40+20
        self.position_needle = self.Sprite.index[4].get_rect(center=(a_x, b_x))
        c_x = self.maze.lst_obj[1].x_position*40+20
        d_x = self.maze.lst_obj[1].y_position*40+20
        self.position_ether = self.Sprite.index[3].get_rect(center=(c_x, d_x))
        e_x = self.maze.lst_obj[2].x_position*40+20
        f_x = self.maze.lst_obj[2].y_position*40+20
        self.position_plastic_tube =\
                              self.Sprite.index[5].get_rect(center=(e_x, f_x))

    def run(self):
        """ start loop """
        loop = True
        while loop is True:
            self.window_surface.blit(self.Sprite.index[6], (0, 0))
            self.pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_F1:
                        loop = False
                    elif event.key == K_ESCAPE:
                        sys.exit(1)

        while(1):
            self.display_map()
            self.event()

    def event(self):
        """ travel and event management """
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:

                if event.key == K_DOWN and\
                                   self.maze.map[self.mcx + 1][self.mcy] != "x":
                    self.position_perso = self.position_perso.move(0, 40)
                    self.mcx = self.mcx + 1
                elif event.key == K_UP and\
                                   self.maze.map[self.mcx - 1][self.mcy] != "x":
                    self.position_perso = self.position_perso.move(0, -40)
                    self.mcx = self.mcx-1
                elif event.key == K_LEFT and\
                                   self.maze.map[self.mcx][self.mcy - 1] != "x":
                    self.position_perso = self.position_perso.move(-40, 0)
                    self.mcy = self.mcy - 1
                elif event.key == K_RIGHT and\
                                     self.maze.map[self.mcx][self.mcy+1] != "x":
                    self.position_perso = self.position_perso.move(40, 0)
                    self.mcy = self.mcy+1

            if self.position_perso.colliderect(self.position_needle):
                self.maze.McGyver.lst_obj[0] = True

            if self.position_perso.colliderect(self.position_ether):
                self.maze.McGyver.lst_obj[1] = True

            if self.position_perso.colliderect(self.position_plastic_tube):
                self.maze.McGyver.lst_obj[2] = True

            if self.position_perso.colliderect(self.position_guard) and\
                                       (self.maze.McGyver.lst_obj[0] == True and
                                        self.maze.McGyver.lst_obj[1] == True and
                                        self.maze.McGyver.lst_obj[2] == True):
                self.print_end_screen(self.Sprite.index[7])
            elif self.position_perso.colliderect(self.position_guard) and\
                                       (self.maze.McGyver.lst_obj[0] == False or
                                        self.maze.McGyver.lst_obj[1] == False or
                                        self.maze.McGyver.lst_obj[2] == False):
                self.print_end_screen(self.Sprite.index[8])

    def print_end_screen(self, Sprite):
        """ display of the end screen """
        while True:
            self.window_surface.blit(Sprite, (0, 0))
            self.pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(-1)

    def display_map(self):
        """ display of map elements and inventory management """

        for data in self.maze.empty_lst:
            self.window_surface.blit(self.Sprite.index[0], data)
        for data in self.maze.wall_lst:
            self.window_surface.blit(self.wall, data)
        if self.maze.McGyver.lst_obj[0] == False:
            self.window_surface.blit(self.Sprite.index[4], self.position_needle)
        if self.maze.McGyver.lst_obj[1] == False:
            self.window_surface.blit(self.Sprite.index[3], self.position_ether)
        if self.maze.McGyver.lst_obj[2] == False:
            self.window_surface.blit(self.Sprite.index[5],
                                     self.position_plastic_tube)
        if self.maze.McGyver.lst_obj[0] == True:
            self.window_surface.blit(self.Sprite.index[4], self.position_rect)
        if self.maze.McGyver.lst_obj[1] == True:
            self.window_surface.blit(self.Sprite.index[3], self.position_rect2)
        if self.maze.McGyver.lst_obj[2] == True:
            self.window_surface.blit(self.Sprite.index[5],
                                     self.position_rect3)

        self.window_surface.blit(self.Sprite.index[1], self.position_perso)
        self.window_surface.blit(self.Sprite.index[2], self.position_guard)
        self.pygame.display.flip()

if __name__ == '__main__':
    Gui = Gui()

Gui.run()
