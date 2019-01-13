#! /usr/bin/env python3
# coding: utf-8
# pylint: disable=no-member
""" setting up the game """

import sys
import pygame
from pygame.draw import rect
from maze import Maze as mz
from sprite import Sprite


# usefull game dimension
TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 15


class Gui(object):
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
        self.sprite = Sprite(self.pygame)
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
        self.position_perso = self.sprite.index[1].get_rect(center=(540, 540))
        self.position_guard = self.sprite.index[2].get_rect(center=(60, 60))
        self.position_rect = self.sprite.index[4].get_rect(center=(320, 620))
        self.position_rect2 = self.sprite.index[3].get_rect(center=(280, 620))
        self.position_rect3 =\
            self.sprite.index[5].get_rect(center=(240, 620))
        a_x = (self.maze.lst_obj[0].x_position)*40+20
        b_x = self.maze.lst_obj[0].y_position*40+20
        self.position_needle = self.sprite.index[4].get_rect(center=(a_x, b_x))
        c_x = self.maze.lst_obj[1].x_position*40+20
        d_x = self.maze.lst_obj[1].y_position*40+20
        self.position_ether = self.sprite.index[3].get_rect(center=(c_x, d_x))
        e_x = self.maze.lst_obj[2].x_position*40+20
        f_x = self.maze.lst_obj[2].y_position*40+20
        self.position_plastic_tube =\
            self.sprite.index[5].get_rect(center=(e_x, f_x))

    def run(self):
        """ start loop """
        loop = True
        while loop is True:
            self.window_surface.blit(self.sprite.index[6], (0, 0))
            self.pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        loop = False
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit(1)
        while 1:
            self.display_map()
            self.event()

    def event(self):
        """ travel and event management """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and\
                        self.maze.map[self.mcx + 1][self.mcy] != "x":
                    self.position_perso = self.position_perso.move(0, 40)
                    self.mcx = self.mcx + 1
                elif event.key == pygame.K_UP and\
                        self.maze.map[self.mcx - 1][self.mcy] != "x":
                    self.position_perso = self.position_perso.move(0, -40)
                    self.mcx = self.mcx-1
                elif event.key == pygame.K_LEFT and\
                        self.maze.map[self.mcx][self.mcy - 1] != "x":
                    self.position_perso = self.position_perso.move(-40, 0)
                    self.mcy = self.mcy - 1
                elif event.key == pygame.K_RIGHT and\
                        self.maze.map[self.mcx][self.mcy+1] != "x":
                    self.position_perso = self.position_perso.move(40, 0)
                    self.mcy = self.mcy+1

            if self.position_perso.colliderect(self.position_needle):
                self.maze.mc_gyver.lst_obj[0] = True

            if self.position_perso.colliderect(self.position_ether):
                self.maze.mc_gyver.lst_obj[1] = True

            if self.position_perso.colliderect(self.position_plastic_tube):
                self.maze.mc_gyver.lst_obj[2] = True

            if self.position_perso.colliderect(self.position_guard) and\
                (self.maze.mc_gyver.lst_obj[0] is True and
                 self.maze.mc_gyver.lst_obj[1] is True and
                 self.maze.mc_gyver.lst_obj[2] is True):
                self.print_end_screen(self.sprite.index[7])
            elif self.position_perso.colliderect(self.position_guard) and\
                (self.maze.mc_gyver.lst_obj[0] is False or
                 self.maze.mc_gyver.lst_obj[1] is False or
                 self.maze.mc_gyver.lst_obj[2] is False):
                self.print_end_screen(self.sprite.index[8])

    def print_end_screen(self, sprite):
        """ display of the end screen """
        while True:
            self.window_surface.blit(sprite, (0, 0))
            self.pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(-1)

    def display_map(self):
        """ display of map elements and inventory management """
        for data in self.maze.empty_lst:
            self.window_surface.blit(self.sprite.index[0], data)
        for data in self.maze.wall_lst:
            self.window_surface.blit(self.wall, data)
        if self.maze.mc_gyver.lst_obj[0] is False:
            self.window_surface.blit(self.sprite.index[4], self.position_needle)
        if self.maze.mc_gyver.lst_obj[1] is False:
            self.window_surface.blit(self.sprite.index[3], self.position_ether)
        if self.maze.mc_gyver.lst_obj[2] is False:
            self.window_surface.blit(self.sprite.index[5],
                                     self.position_plastic_tube)
        if self.maze.mc_gyver.lst_obj[0] is True:
            self.window_surface.blit(self.sprite.index[4], self.position_rect)
        if self.maze.mc_gyver.lst_obj[1] is True:
            self.window_surface.blit(self.sprite.index[3], self.position_rect2)
        if self.maze.mc_gyver.lst_obj[2] is True:
            self.window_surface.blit(self.sprite.index[5],
                                     self.position_rect3)
        self.window_surface.blit(self.sprite.index[1], self.position_perso)
        self.window_surface.blit(self.sprite.index[2], self.position_guard)
        self.pygame.display.flip()

if __name__ == '__main__':
    GUI = Gui()
    GUI.run()
