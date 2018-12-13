import pygame, sys
from pygame.locals import *
from parse import *
from sprite import *

class Maze:

    self.map = map
    self.McGyver = sprite.MacGyver.get_rect(center=(540, 540))
    self.Murdock = sprite.Guardian.get_rect(center=(60, 60))
    self.lstObj =

    def user_input(self, pygame):
        continue_game = 1
        continue_home = 1

        while continue_home:

            for event in pygame.event.get():
                #press escape to leave the game
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continue_home = 0
                    continue_game = 0
                    continuer = 0
                #press F1 to start the game
                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        continue_home = 0
                        continue_game = 1


        if event.type == KEYDOWN:

            if event.key == K_DOWN and map[mcx+1][mcy]!= "x":
                position_perso = position_perso.move(0, 40)
                mcx = mcx+1
            elif event.key == K_UP and map[mcx-1][mcy]!= "x":
                position_perso = position_perso.move(0, -40)
                mcx = mcx-1
            elif event.key == K_LEFT and map[mcx][mcy-1]!= "x":
                position_perso = position_perso.move(-40, 0)
                mcy = mcy-1
            elif event.key == K_RIGHT and map[mcx][mcy+1]!= "x":
                position_perso = position_perso.move(40, 0)
                mcy = mcy+1

    def game_loop():

    def show_items():

    def victory_conditions():

class McGyver:

class objet:

class Murdock:
