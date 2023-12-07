import os
import pygame

def loadFont(name,size):
    working_dir = os.path.dirname(__file__)
    full_path = working_dir + "/font/" + name
    return pygame.font.Font(full_path,size)

def get_rgb(hexcolor):
    return tuple(int(hexcolor[1:][i:i+2], 16) for i in (0,2,4))