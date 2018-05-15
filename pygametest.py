import pygame
import sys

def createScreen(dimmensions):
    pygame.init()

    w = 70
    x = 0
    y = 0
    grid = [[1]*dimmensions for n in range(dimmensions)]
    
    BackGround = pygame.image.load('Images/grass-pattern.png')
    tree = pygame.image.load('Images/tree_sized.png')
    screen = pygame.display.set_mode((w*dimmensions,w*dimmensions))

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

createScreen(15)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location