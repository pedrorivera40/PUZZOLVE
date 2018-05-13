from pygame.locals import *
import pygame


class Player:
    x = 44
    y = 44
    speed = 5

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed


class Maze:
    def __init__(self):
        self.M = 10
        self.N = 8
        self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]

    def draw(self, display_surf, image_surf):
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            if self.maze[bx + (by * self.M)] == 1:
                display_surf.blit(image_surf, (bx * 44, by * 44))

            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1


class App:

    windowWidth = 800
    windowHeight = 600
    player = 0
    clock = pygame.time.Clock()

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()
        self.Background = None
        self.images_dict = {
            'RIGHT': [],
            'LEFT': [],
            'UP': [],
            'DOWN': []
        }
        self.counter = 0

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self.Background = pygame.image.load("Images/grass-pattern.png").convert()
        self.images_dict['DOWN'].append(pygame.image.load("Images/ironman_front.png"))
        self.images_dict['DOWN'].append(pygame.image.load("Images/ironman_front1.png"))
        self.images_dict['DOWN'].append(pygame.image.load("Images/ironman_front2.png"))
        self.images_dict['LEFT'].append(pygame.image.load("Images/ironman_left.png"))
        self.images_dict['LEFT'].append(pygame.image.load("Images/ironman_left1.png"))
        self.images_dict['LEFT'].append(pygame.image.load("Images/ironman_left2.png"))
        self.images_dict['UP'].append(pygame.image.load("Images/ironman_back.png"))
        self.images_dict['UP'].append(pygame.image.load("Images/ironman_back1.png"))
        self.images_dict['UP'].append(pygame.image.load("Images/ironman_back2.png"))
        self.images_dict['RIGHT'].append(pygame.image.load("Images/ironman_right.png"))
        self.images_dict['RIGHT'].append(pygame.image.load("Images/ironman_right1.png"))
        self.images_dict['RIGHT'].append(pygame.image.load("Images/ironman_right2.png"))
        self._image_surf = self.images_dict['DOWN'][0]
        self._image_surf = pygame.transform.rotozoom(self._image_surf, 0, 1.5)

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def switch_image(self, direction, index):
        if direction == "RIGHT":
            self._image_surf = self.images_dict['RIGHT'][index]

        if direction == "LEFT":
            self._image_surf = self.images_dict['LEFT'][index]

        if direction == "DOWN":
            self._image_surf = self.images_dict['DOWN'][index]

        if direction == "UP":
            self._image_surf = self.images_dict['UP'][index]

        self._image_surf = pygame.transform.rotozoom(self._image_surf, 0, 1.5)

    def on_render(self):
        self._display_surf.blit(self.Background, (0, 0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self._running = False

            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.switch_image("RIGHT", self.counter)
                self.counter = (self.counter + 1) % len(self.images_dict['RIGHT'])
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.switch_image("LEFT", self.counter)
                self.counter = (self.counter + 1) % len(self.images_dict['LEFT'])
                self.player.moveLeft()

            if (keys[K_UP]):
                self.switch_image("UP", self.counter)
                self.counter = (self.counter + 1) % len(self.images_dict['UP'])
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.switch_image("DOWN", self.counter)
                self.counter = (self.counter + 1) % len(self.images_dict['DOWN'])
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
            self.clock.tick(15)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
