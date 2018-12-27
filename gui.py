from Sprite import *
import pygame, sys
from pygame.locals import *
from pygame.draw import *
from classes import Maze as mz


#usefull game dimension
TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 15

# set up pygame
class gui:
    def __init__(self):
        self.mcx = 13
        self.mcy = 13
        self.position_perso = [520,520]
        self.maze = mz()
        self.pygame = pygame
        self.pygame.init()
        self.init_ui()
        self.pygame.font.init()
        self.myfont = self.pygame.font.SysFont('monospace', 16)
        self.sprite = sprite(self.pygame)

        self.rectangle = self.pygame.draw.rect(self.windowSurface, (255,255,255), (0, 80, 0, 40))
        self.init_music()
        self.init_sprite()
        self.wall = pygame.image.load("tile.png").convert()


    def init_music(self):
        self.pygame.mixer.music.load('macgyver-theme-song.ogg')
        self.pygame.mixer.music.play(0)
        self.pygame.mixer.music.set_volume(0.0)
        self.pygame.mixer.music.unpause()



# set up the window
    def init_ui(self):
        self.windowSurface = self.pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 40), 0, 32)
        #self.pygame.display.set_caption('Mac Gyver')


        #sprite = sprite(self.pygame)


# load wall image
        #WALL = self.pygame.image.load('tile.png').convert()
    def init_sprite(self):
        self.position_perso = self.sprite.MacGyver.get_rect(center=(540, 540))
        self.position_guard = self.sprite.Guardian.get_rect(center=(60, 60))
        self.position_rect = self.sprite.needle.get_rect(center=(320, 620))
        self.position_rect2 = self.sprite.ether.get_rect(center=(280, 620))
        self.position_rect3 = self.sprite.plastic_tube.get_rect(center=(240, 620))
        print(self.maze.lstObj[0].x)
        ax = (self.maze.lstObj[0].x)*40+20
        bx = self.maze.lstObj[0].y*40+20
        self.position_needle = self.sprite.needle.get_rect(center=(ax,bx))
        cx = self.maze.lstObj[1].x*40+20
        dx = self.maze.lstObj[1].y*40+20
        self.position_ether = self.sprite.ether.get_rect(center=(cx, dx))
        ex = self.maze.lstObj[2].x*40+20
        fx = self.maze.lstObj[2].y*40+20
        self.position_plastic_tube = self.sprite.plastic_tube.get_rect(center=(ex, fx))



    def run(self):
        while(1):
            self.display_map()
            self.event()

    def event(self):
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

            if self.position_perso.colliderect(self.position_guard) and self.maze.McGyver.lstObj[0] == True and self.maze.McGyver.lstObj[1] == True and self.maze.McGyver.lstObj[2] == True:
                self.windowSurface.blit(self.sprite.congratulations, (0,0))
            elif self.position_perso.colliderect(self.position_guard) and (self.maze.McGyver.lstObj[0] == False or self.maze.McGyver.lstObj[1] == False or self.maze.McGyver.lstObj[2] == False):
                self.windowSurface.blit(self.sprite.game_over, (0,0))

    def display_map(self):

        for data in self.maze.empty_lst:
            self.windowSurface.blit(self.sprite.Floor, data)
        for data in self.maze.wall_lst:

            self.windowSurface.blit(self.wall, data)
        if self.maze.McGyver.lstObj[0]== False:
            self.windowSurface.blit(self.sprite.needle, self.position_needle)
        if self.maze.McGyver.lstObj[1]== False:
            self.windowSurface.blit(self.sprite.ether, self.position_ether)
        if self.maze.McGyver.lstObj[2]== False:
            self.windowSurface.blit(self.sprite.plastic_tube, self.position_plastic_tube)



        self.windowSurface.blit(self.sprite.MacGyver, self.position_perso)
        self.windowSurface.blit(self.sprite.Guardian, self.position_guard)
        # if inventory[0] ==  False:
        #     self.windowSurface.blit(sprite.needle, position_needle)
        # if inventory[1] ==  False:
        #     self.windowSurface.blit(sprite.ether, position_ether)
        # if inventory[2] ==  False:
        #     self.windowSurface.blit(sprite.plastic_tube, position_plastic_tube)
        # if inventory[0] == True:
        #     self.windowSurface.blit(sprite.needle, position_rect)
        # if inventory[1] == True:
        #     self.windowSurface.blit(sprite.ether, position_rect2)
        # if inventory[2] == True:
        #     self.windowSurface.blit(sprite.plastic_tube, position_rect3)


        self.pygame.display.flip()

if __name__ == '__main__':
    gui = gui()

    gui.run()
