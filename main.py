import pygame
import pygame_widgets
from pygame_widgets.button import Button
from helper import *
from sys import exit

# Pygame Admin 
pygame.init()
pygame.display.set_caption("Tic Tac Toe")
SCR_WIDTH = SCR_HEIGHT = 600
screen = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
clock = pygame.time.Clock()
game_active = False

# Colours
white = (255,255,255)
black = (0,0,0)
blue = get_rgb('#5271FF')
gray = get_rgb('#A6A6A6')

# Fonts
boldsans50 = loadFont("opensansbold.ttf", 50) 
regularsans22 = loadFont("opensansregular.ttf", 22)

# Fill white colour as background
screen.fill(white)

# Non-Active Game Elements
title = boldsans50.render("Tic Tac Toe", False, black)
title_rect = title.get_rect(center = (300,70))


selected = True

def button1Clicked():
    global selected
    selected = True

def button2Clicked():
    global selected
    selected = False

button1 = Button(screen, (SCR_WIDTH - 350)//2, 200, 350, 50, 
                text="Human vs Human",
                font=regularsans22,
                inactiveColour=blue if selected else gray,
                hoverColour=blue,
                pressedColour=blue,
                textColour=white,
                textHAlign='center',
                textVAlign='center',
                onClick=button1Clicked)

button2 = Button(screen, (SCR_WIDTH - 350)//2, 270, 350, 50, 
                text="Human vs Computer",
                font=regularsans22,
                inactiveColour=gray if selected else blue,
                hoverColour=blue,
                pressedColour=blue,
                textColour=white,
                textHAlign='center',
                textVAlign='center',
                onClick=button2Clicked)

# Main Loop
while True:
    
    events = pygame.event.get()

    # loop to check for events
    for event in events:

        # QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()    

    if not game_active:

        button1.setInactiveColour(blue if selected else gray)
        button2.setInactiveColour(gray if selected else blue)
        screen.blit(title, title_rect)

    pygame_widgets.update(events)
    pygame.display.update()
    clock.tick_busy_loop(60)
