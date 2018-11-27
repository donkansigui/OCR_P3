from pygame.draw import *
import pygame, sys
from pygame.locals import *
from parse import *
from random import *






# set up pygame
pygame.init()

# fonction qui retourne un emplacement aleatoire sur la liste "map"
print("---------------")
def alea(map):
    x = randint(1, 13)
    y = randint (1, 13)
    print(x)
    print(y)
    print (map [x][y])
    if map [y][x] == "x":
        return alea(map)
    ret = (y,x)
    return ret
# variables
needle_xy = alea(map)
ether_xy = alea(map)
plastic_tube_xy = alea(map)


# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (174, 40, 171)

#usefull game dimension
TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 15


# set up the window
windowSurface = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE), 0, 32)
pygame.display.set_caption('Mac Gyver')

FLOOR = pygame.image.load('floor.png').convert()

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

# load image
MacGyver = pygame.image.load('MacGyver.png').convert_alpha()
Guardian = pygame.image.load('Guardian.png').convert_alpha()
ether = pygame.image.load('ether.png').convert_alpha()
needle = pygame.image.load('needle.png').convert()
plastic_tube = pygame.image.load('plastic_tube.png').convert()

# set up positioning
position_perso = MacGyver.get_rect(center=(540, 540))
position_guard = Guardian.get_rect(center=(60, 60))
ax = needle_xy[0]*40+20
bx = needle_xy[1]*40+20
position_needle = needle.get_rect(center=(ax,bx))
cx = ether_xy[0]*40+20
dx = ether_xy[1]*40+20
position_ether = ether.get_rect(center=(cx, dx))
ex = plastic_tube_xy[0]*40+20
fx = plastic_tube_xy[0]*40+20
position_plastic_tube = ether.get_rect(center=(ex, fx))
# show image



# load wall image
WALL = pygame.image.load('tile.png').convert()
WALL_LST = []
i = 0

# add walls
for line in map:
    j = 0
    for square in line:
        position = (j*40, i*40)
        if square == "x":
            WALL_LST.append(position)

        j=j+1
    i = i+1

# a definir
mcx = 13
mcy = 13




# le compteur prend la position de mac et ajoute a la liste quand mac passe sur un objet



# ajout de global pour les variables
#global position_perso
#mac = position_perso
#global position_needle
#needle = position_needle
#global position_ether
#ether = position_ether
#global position_plastic_tube
#tube = position_plastic_tube
#if mac == needle:
#    counter.append("needle")
#elif mac == ether:
#    counter.append("ether")
#elif mac == tube:
#    counter.append("tube")

#compteur
counter = ""

if position_perso.colliderect(position_needle):
    counter += "needle"
elif position_perso.colliderect(position_ether):
    counter += "ether"
elif position_perso.colliderect(position_plastic_tube):
    counter += "tube"

counter_display = basicFont.render(counter, 1, (255,255,0))
# needle, ether, tube
inventory = [False, False, False]



# run the game loop
continuer = 1

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
            print("Congratulation")
        elif position_perso.colliderect(position_guard) and (inventory[0] == False or inventory[1] == False or inventory[2] == False):
            print("Game over")


        #if event.type == KEYDOWN and position_perso == position_needle:
        #    print("yup")
        #if event.type == KEYDOWN and position_perso == position_ether:
        #    print("ether")
        #if event.type == KEYDOWN and position_perso == position_plastic_tube:
        #    print("plastic")
        #if event.type == KEYDOWN and position_perso == position_guard:
        #    print("congrat")




    windowSurface.blit(FLOOR, (0,0))
    windowSurface.blit(MacGyver, position_perso)
    windowSurface.blit(Guardian, position_guard)
    if inventory[0] ==  False:
        windowSurface.blit(needle, position_needle)
    if inventory[1] ==  False:
        windowSurface.blit(ether, position_ether)
    if inventory[2] ==  False:
        windowSurface.blit(plastic_tube, position_plastic_tube)
    for data in WALL_LST:
        windowSurface.blit(WALL, data)
    #windowSurface.blit(counter_display, (100,100))


    pygame.display.flip()
