import pygame
import sys
import numpy as np



class Screen():
   
    def __init__(self,square =10):
        self.square = square 
        # initially the matrix will contain zeros
        # if there is an obstacle the position in the matrix will contain a one
        self.obstacle_matrix = np.matrix(np.zeros((square,square)))
        
    def createScreen(self,dimensions):
        pygame.init()
        w = 70
        x = 0
        y = 0
        grid = [[1]*dimensions for n in range(dimensions)]
    
        BackGround = pygame.image.load('Images/grass-pattern.png')
        tree = pygame.image.load('Images/tree_sized.png')
        screen = pygame.display.set_mode((w*dimensions,w*dimensions))

        screen.fill((255,255,255))
        screen.blit(BackGround, [0,0])

        for row in grid:
            for column in row:
                pygame.draw.rect(screen,(0,0,0),(x,y, w,w),1)
                x = x+ w
            y = y + w
            x = 0

        screen.blit(tree, [0,0])
        screen.blit(tree, [w*8,w*5])


        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 

screen = Screen(10)
screen.createScreen(10)

 

