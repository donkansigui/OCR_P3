from pygame import *

class sprite:
    def __init__(self, pygame):

        self.Floor = pygame.image.load('floor.png').convert()

        # set up fonts
        self.basicFont = pygame.font.SysFont(None, 48)

    # load image
        self.MacGyver = pygame.image.load('MacGyver.png').convert_alpha()
        self.Guardian = pygame.image.load('Guardian.png').convert_alpha()
        self.ether = pygame.image.load('ether.png').convert_alpha()
        self.needle = pygame.image.load('needle.png').convert()
        self.plastic_tube = pygame.image.load('plastic_tube.png').convert()
        self.home = pygame.image.load('Mc_Gyver.png').convert()
