from Tkinter import *
import Tkinter as tk
import pygame
from pygame.locals import *
import os

def set_screen():
    global screen

    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((600,600))
    screen_rect = screen.get_rect()
    pygame.draw.circle(screen, (255,0,0), screen_rect.center, 50 )
    pygame.display.flip()


def set_tk():
    global root
    global embed
    global tkwin
    root = tk.Tk()
    root.wm_title("PUZZOLVE")
    embed = tk.Frame(root, width = 600, height = 600)
    embed.pack(side=LEFT)
    windowid = embed.winfo_id()

    # embed tk window
    tkwin = tk.Frame(root, width = 200, height = 600)
    tkwin.pack(side=TOP)

    # Embedd terminal window.
    # termf = Frame(root, height=400, width=500)
    # termf.pack(side=BOTTOM,fill=BOTH, expand=YES)
    # wid = termf.winfo_id()
    # os.system('xterm -into %d -geometry 400x500 -sb &' % wid)

    os.environ['SDL_WINDOWID'] = str(windowid)
    root.after(100,set_screen)
    root.mainloop()

set_tk()