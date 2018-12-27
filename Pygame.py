from pygame.draw import *
import pygame, sys
from pygame.locals import *
from parse import *
import random
from Sprite import *



# variables
needle_xy = pos[0]
OBJECT_POS.append(needle_xy)
ether_xy = pos[1]
OBJECT_POS.append(ether_xy)
plastic_tube_xy = pos[2]
OBJECT_POS.append(plastic_tube_xy)
print (ether_xy, "[", map[int(ether_xy[0])][int(ether_xy[1])])
print (plastic_tube_xy, "[", map[int(plastic_tube_xy[0])][int(plastic_tube_xy[1])])
print (needle_xy, "[" , map[int(needle_xy[0])][int(needle_xy[1])])



#rectangleee = pygame.draw.rect(windowSurface, (255,255,255), (0, 520, 0,  260))
# set up positioning


# variables
mcx = 13
mcy = 13


#fonts


#rectangleee = pygame.draw.rect(windowSurface, (255,255,255), (0, 520, 0,  260))
# needle, ether, tube
inventory = [False, False, False]

#main loop
continuer = 1
while continuer:
    #loading and viewing the home screen
    home = sprite.home
    windowSurface.blit(home, (0,0))

    #refresh
    pygame.display.flip()
    #These variables are reset to 1 at each loop turn
    continue_game = 1
    continue_home = 1

    #home loop
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


    #run the game loop
    while continuer:


        windowSurface.blit(sprite.Floor, (0,0))
        windowSurface.blit(sprite.MacGyver, position_perso)
        windowSurface.blit(sprite.Guardian, position_guard)
        for data in WALL_LST:
            windowSurface.blit(WALL, data)

        if inventory[0] ==  False:
            windowSurface.blit(sprite.needle, position_needle)
        if inventory[1] ==  False:
            windowSurface.blit(sprite.ether, position_ether)
        if inventory[2] ==  False:
            windowSurface.blit(sprite.plastic_tube, position_plastic_tube)
        if inventory[0] == True:
            windowSurface.blit(sprite.needle, position_rect)
        if inventory[1] == True:
            windowSurface.blit(sprite.ether, position_rect2)
        if inventory[2] == True:
            windowSurface.blit(sprite.plastic_tube, position_rect3)


        pygame.display.flip()
