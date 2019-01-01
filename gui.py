#! /usr/bin/env python3
# coding: utf-8

import pygame
import sys
from pygame.locals import *
from pygame.draw import *
from classes import Maze as mz
from Sprite import *


#usefull game dimension
TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 15


class Gui:
    """ setting up the game """
    def __init__(self):
        """ setting up values """
        self.mcx = 13
        self.mcy = 13
        self.position_perso = [520,520]
        self.maze = mz()
        self.pygame = pygame
        self.pygame.init()
        self.init_ui()
        self.pygame.font.init()
        self.myfont = self.pygame.font.SysFont('monospace', 16)
        self.Sprite = Sprite(self.pygame)

        self.rectangle = self.pygame.draw.rect(self.windowSurface, (255,255,255), (0, 80, 0, 40))
        self.init_music()
        self.init_Sprite()
        self.wall = pygame.image.load("tile.png").convert()

    def init_music(self):
        """ setting up the music """
        self.pygame.mixer.music.load('macgyver-theme-song.ogg')
        self.pygame.mixer.music.play(-1)
        self.pygame.mixer.music.set_volume(0.6)
        self.pygame.mixer.music.unpause()

    def init_ui(self):
        """ setting up the main window """
        self.windowSurface = self.pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 40), 0, 32)
        self.pygame.display.set_caption('Mac Gyver')

    def init_Sprite(self):
        """ setting up sprites positioning """
        self.position_perso = self.Sprite.MacGyver.get_rect(center=(540, 540))
        self.position_guard = self.Sprite.Guardian.get_rect(center=(60, 60))
        self.position_rect = self.Sprite.needle.get_rect(center=(320, 620))
        self.position_rect2 = self.Sprite.ether.get_rect(center=(280, 620))
        self.position_rect3 = self.Sprite.plastic_tube.get_rect(center=(240, 620))
        print(self.maze.lstObj[0].x)
        ax = (self.maze.lstObj[0].x)*40+20
        bx = self.maze.lstObj[0].y*40+20
        self.position_needle = self.Sprite.needle.get_rect(center=(ax,bx))
        cx = self.maze.lstObj[1].x*40+20
        dx = self.maze.lstObj[1].y*40+20
        self.position_ether = self.Sprite.ether.get_rect(center=(cx, dx))
        ex = self.maze.lstObj[2].x*40+20
        fx = self.maze.lstObj[2].y*40+20
        self.position_plastic_tube = self.Sprite.plastic_tube.get_rect(center=(ex, fx))

    def run(self):
        """ start loop """
        while(1):
            self.display_map()
            self.event()

    def event(self):
        """ travel and event management """
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:

                if event.key == K_DOWN and self.maze.map[self.mcx+1][self.mcy]!= "x":
                    self.position_perso = self.position_perso.move(0, 40)
                    self.mcx = self.mcx+1
                elif event.key == K_UP and self.maze.map[self.mcx-1][self.mcy]!= "x":
                    self.position_perso = self.position_perso.move(0, -40)
                    self.mcx = self.mcx-1
                elif event.key == K_LEFT and self.maze.map[self.mcx][self.mcy-1]!= "x":
                    self.position_perso = self.position_perso.move(-40, 0)
                    self.mcy = self.mcy-1
                elif event.key == K_RIGHT and self.maze.map[self.mcx][self.mcy+1]!= "x":
                    self.position_perso = self.position_perso.move(40, 0)
                    self.mcy = self.mcy+1

            if self.position_perso.colliderect(self.position_needle):
                self.maze.McGyver.lstObj [0] = True

            if self.position_perso.colliderect(self.position_ether):
                self.maze.McGyver.lstObj [1] = True

            if self.position_perso.colliderect(self.position_plastic_tube):
                self.maze.McGyver.lstObj [2] = True

            if self.position_perso.colliderect(self.position_guard) and (self.maze.McGyver.lstObj[0] == True and self.maze.McGyver.lstObj[1] == True and self.maze.McGyver.lstObj[2] == True):
                self.print_end_screen(self.Sprite.congratulations)
            elif self.position_perso.colliderect(self.position_guard) and (self.maze.McGyver.lstObj[0] == False or self.maze.McGyver.lstObj[1] == False or self.maze.McGyver.lstObj[2] == False):
                self.print_end_screen(self.Sprite.game_over)

    def print_end_screen(self, Sprite):
        """ display of the end screen """
        while True:
            self.windowSurface.blit(Sprite, (0, 0))
            self.pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(-1)

    # def print_home_screen(self, Sprite):
    #     while True:
    #         self.windowSurface.blit(Sprite, (0, 0))
    #         self.pygame.display.flip()
    #         for event in pygame.event.get():
    #             if event.type == KEYDOWN:
    #                 if event.key == K_F1:




    def display_map(self):
        """ display of map elements and inventory management """

        for data in self.maze.empty_lst:
            self.windowSurface.blit(self.Sprite.Floor, data)
        for data in self.maze.wall_lst:
            self.windowSurface.blit(self.wall, data)
        if self.maze.McGyver.lstObj[0]== False:
            self.windowSurface.blit(self.Sprite.needle, self.position_needle)
        if self.maze.McGyver.lstObj[1]== False:
            self.windowSurface.blit(self.Sprite.ether, self.position_ether)
        if self.maze.McGyver.lstObj[2]== False:
            self.windowSurface.blit(self.Sprite.plastic_tube, self.position_plastic_tube)
        if self.maze.McGyver.lstObj[0]== True:
            self.windowSurface.blit(self.Sprite.needle, self.position_rect)
        if self.maze.McGyver.lstObj[1]== True:
            self.windowSurface.blit(self.Sprite.ether, self.position_rect2)
        if self.maze.McGyver.lstObj[2]== True:
            self.windowSurface.blit(self.Sprite.plastic_tube, self.position_rect3)

        self.windowSurface.blit(self.Sprite.MacGyver, self.position_perso)
        self.windowSurface.blit(self.Sprite.Guardian, self.position_guard)
        self.pygame.display.flip()

if __name__ == '__main__':
    Gui = Gui()

    Gui.run()
