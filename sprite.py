from pygame import *


class Sprite:
    """ assignment of images """
    def __init__(self, pygame):
        """ importing images using the pygame library """

        self.index = {}
        self.index[0] = pygame.image.load('./pictures/floor.png').convert()
        self.index[1] = pygame.image.load('./pictures/macgyver.png').convert_alpha()
        self.index[2] = pygame.image.load('./pictures/guardian.png').convert_alpha()
        self.index[3] = pygame.image.load('./pictures/ether.png').convert_alpha()
        self.index[4] = pygame.image.load('./pictures/needle.png').convert()
        self.index[5] = pygame.image.load('./pictures/plastic_tube.png').convert()
        self.index[6] = pygame.image.load('./pictures/mc_gyver.png').convert()
        self.index[7] = pygame.image.load('./pictures/the_end.png').convert()
        self.index[8] = pygame.image.load('./pictures/game_over.png').convert()

        # self.floor = pygame.image.load('./pictures/floor.png').convert()

        # set up fonts
        self.basic_font = pygame.font.SysFont(None, 48)

        # self.macgyver = pygame.image.load('./pictures/macgyver.png').convert_alpha()
        # self.guardian = pygame.image.load('./pictures/guardian.png').convert_alpha()
        # self.ether = pygame.image.load('./pictures/ether.png').convert_alpha()
        # self.needle = pygame.image.load('./pictures/needle.png').convert()
        # self.plastic_tube = pygame.image.load('./pictures/plastic_tube.png').convert()
        # self.home = pygame.image.load('./pictures/mc_gyver.png').convert()
        # self.congratulations = pygame.image.load('./pictures/the_end.png').convert()
        # self.game_over = pygame.image.load('./pictures/game_over.png').convert()
