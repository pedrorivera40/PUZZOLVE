import pygame
import sys

def createScreen(dimmensions):
    pygame.init()

    x = 0
    y = 0
    grid = [[1]*dimmensions for n in range(dimmensions)]
    w = 70

    screen = pygame.display.set_mode((w*dimmensions,w*dimmensions))

    screen.fill((255,255,255))

    for row in grid:
        for column in row:
            pygame.draw.rect(screen,(0,0,0),(x,y, w,w),1)
            x = x+ w
        y = y + w
        x = 0



    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

createScreen(12)