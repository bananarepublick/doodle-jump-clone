import pygame, sys
from pygame.locals import *

pygame.init()

class Player:
    #variables
    x = 0
    y = 0
    gravity = 9
    GREEN = pygame.Color(72, 244, 66)
    SURFACE = None
    doodle = pygame.image.load("doodle.png")


    def __init__(self, surface):
        """"Constructor function that takes the surface to be drawn on as an argument"""
        self.SURFACE = surface
        self.x = self.SURFACE.get_width() / 2
        self.y = self.SURFACE.get_height() / 2


    def show(self):
        """"Draw Player on the screen at x and y"""
        self.SURFACE.blit(self.doodle, (self.x, self.y))

    def isTouching(self, platform):
        """"Checks if player is touching the platform"""
        #pretty ugly I know
        if self.x >= platform.x and self.x+self.doodle.get_rect().width <= platform.x + platform.width and self.y+self.doodle.get_rect().height == platform.y:
            return True
        else:
            return False

    def move(self, dir):
        """"Function that takes a string dir as an argument and moves the player object accordingly"""
        if dir == "":
            self.y += self.gravity
        elif dir == "RIGHT":
            self.x += 10
        elif dir == "LEFT":
            self.x -= 10
        elif dir == "UP":
            self.y -= self.gravity
        self.SURFACE.fill((255,255,255))
        self.SURFACE.blit(self.doodle, (self.x, self.y))