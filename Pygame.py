from pygame.draw import *
import pygame, sys
from pygame.locals import *
from parse import *
import random
from Sprite import *
from Maze import *

#usefull game dimension
TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 15

# set up pygame
pygame.init()

def init_Music():
    pygame.mixer.music.load('macgyver-theme-song.ogg')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.unpause()



# set up the window
windowSurface = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 40), 0, 32)
pygame.display.set_caption('Mac Gyver')

sprite = sprite(pygame)


# load wall image
WALL = pygame.image.load('tile.png').convert()
WALL_LST = []
EMPTY_LST = []
OBJECT_POS = []
i = 0

# add walls
for line in Maze.map:
    j = 0
    for square in line:
        print(square)
        position = (j*40, i*40)
        positionTab = [j , i ]
        if square == "x":
            WALL_LST.append(position)
            print("dedans")
        elif square == " ":
            EMPTY_LST.append(positionTab)
            print("dehors")
        j=j+1
    i = i+1
for data in EMPTY_LST:
    if data[0] == 3 and data[1] ==3:
        print ("error")
EMPTY_LST.remove([1, 13])
# function for random placement of items
# def random_positioning(map):
#
#     x = randint(0, EMPTY_LST.__len__() - 1)
#     xx = (int(EMPTY_LST[x][0] * 40))
#     yy = (int(EMPTY_LST[x][1] * 40))
#     diff = (xx , yy )
#
#     if map[EMPTY_LST[x][0]][EMPTY_LST[x][1]] == "x":
#            return random_positioning(map)
#     for obj in OBJECT_POS:
#         if obj == diff:
#             return random_positioning(map)
#     for s in WALL_LST:
#         if diff == s:
#             return random_positioning(map)
#     if diff == (520, 40):
#         return random_positioning(map)
#         #idem pour le guard
#     ret = ((xx)/ 40, (yy) / 40)
#     OBJECT_POS.append(diff)
#     return ret

pos = (random.sample(EMPTY_LST, 3))


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
position_perso = sprite.MacGyver.get_rect(center=(540, 540))
position_guard = sprite.Guardian.get_rect(center=(60, 60))
position_rect = sprite.needle.get_rect(center=(320, 620))
position_rect2 = sprite.ether.get_rect(center=(280, 620))
position_rect3 = sprite.plastic_tube.get_rect(center=(240, 620))
ax = needle_xy[0]*40+20
bx = needle_xy[1]*40+20
position_needle = sprite.needle.get_rect(center=(ax,bx))
cx = ether_xy[0]*40+20
dx = ether_xy[1]*40+20
position_ether = sprite.ether.get_rect(center=(cx, dx))
ex = plastic_tube_xy[0]*40+20
fx = plastic_tube_xy[0]*40+20
position_plastic_tube = sprite.plastic_tube.get_rect(center=(ex, fx))


# variables
mcx = 13
mcy = 13


#fonts
pygame.font.init()
myfont = pygame.font.SysFont('monospace', 16)
#variables
SCORE = 0
RUNNING = True
rectangle = pygame.draw.rect(windowSurface, (255,255,255), (0, 80, 0, 40))

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

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
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

            if position_perso.colliderect(position_needle):
                inventory[0] = True

            if position_perso.colliderect(position_ether):
                inventory[1] = True

            if position_perso.colliderect(position_plastic_tube):
                inventory[2] = True

            if position_perso.colliderect(position_guard) and inventory[0] == True and inventory[1] == True and inventory[2] == True:
                print("Congratulations")
            elif position_perso.colliderect(position_guard) and (inventory[0] == False or inventory[1] == False or inventory[2] == False):
                print("Game over")


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
