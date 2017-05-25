import pygame, sys
from pygame.locals import *
from player import *
from platform import *
import random

#colors
WHITE = pygame.Color(255, 255, 255)

#pygame setup
pygame.init()
SURFACE = pygame.display.set_mode((800,600))
pygame.display.set_caption("Doodle Jump")
SURFACE.fill(WHITE)
pygame.key.set_repeat(30,30)
fpsClock = pygame.time.Clock()
FPS = 60
#creating the player object and passing it the SURFACE object
p = Player(SURFACE)
#creating empty platforms array
platforms = []

#fill platforms array
for i in range(SURFACE.get_height()):
    if i % 120 == 0:
        #every 120 pixels in y create a new Platform with a random x position
        platforms.append(Platform(random.randint(0, SURFACE.get_width()), i, SURFACE))

while True: #main game loop

    p.show()
    #eventhandling
    for ev in pygame.event.get():
        #quit event
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()

        #keyhandling
        elif ev.type == KEYDOWN and ev.key == K_RIGHT:
            p.move("RIGHT")
        elif ev.type == KEYDOWN and ev.key == K_LEFT:
            p.move("LEFT")

    #draw platforms on the screen
    for plat in platforms:
        plat.show()
    #move the player up if he's touching the platform
    for pla in platforms:
        if p.isTouching(pla):
           p.move("UP")
    #gravity
    p.move("")

    pygame.display.update()
    fpsClock.tick(FPS)