import pygame
import sys
import numpy as np



class Screen():
   
    def __init__(self,square =10):
        self.square = square 
        # initially the matrix will contain zeros
        # if there is an obstacle the position in the matrix will contain a one
        self.obstacle_matrix = np.matrix(np.zeros((square,square)))
       
       # I don't know wtf this is
        self.w = 70
        self.x = 0
        self.y = 0
        self.screen =  pygame.display.set_mode((self.w*self.square,self.w*self.square))
    def createScreen(self,dimensions):
        pygame.init()
        grid = [[1]*dimensions for n in range(dimensions)]
    
        BackGround = pygame.image.load('Images/grass-pattern.png')
        tree = pygame.image.load('Images/tree_sized.png')

        self.screen.fill((255,255,255))
        self.screen.blit(BackGround, [0,0])

        for row in grid:
            for column in row:
                pygame.draw.rect(self.screen,(0,0,0),(self.x,self.y, self.w,self.w),1)
                self.x = self.x+ self.w
            self.y = self.y + self.w
            self.x = 0

        self.screen.blit(tree, [0,0])
        self.screen.blit(tree, [self.w*8,self.w*5])
        #self.add_obstacle(tree,3,2)

        pygame.display.flip()

        #running = True
       # while running:
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #running = False 
    
    def add_obstacle(self,image,x,y):
        self.obstacle_matrix[y-1,x-1] = 1
        self.screen.blit(image,[self.w*(x-1),self.w*(y-1)])
        pygame.display.update()

def display_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

screen = Screen(10)
screen.createScreen(10)
tree = pygame.image.load('Images/tree_sized.png')
LEFT = 1 
screen.add_obstacle(tree,1,4)
#display_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            screen.add_obstacle(tree,5,5)
            print("Left mouse pressed")
 
#screen = Screen(10)
#screen.createScreen(10)
#tree = pygame.image.load('Images/tree_sized.png')

#screen.add_obstacle(tree,1,4)
#display_screen()
#screen.add_obstacle(tree,6,7)



