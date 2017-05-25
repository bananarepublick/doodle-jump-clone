import pygame, sys
from pygame.locals import *

pygame.init()

class Platform:

    #variables
    x = 0
    y = 0
    height = 25
    width = 120
    SURFACE = None
    ORANGE = pygame.Color(244, 122, 66)
    img = pygame.image.load("platform.png")

    def __init__(self, x, y, surface):
        """"Constructor function that takes x, y and surface as parameters"""
        self.x = x
        self.y = y
        self.SURFACE = surface

    def show(self):
        """"Displays the platform on the screen"""
        self.SURFACE.blit(self.img, (self.x, self.y))