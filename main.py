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

# Colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = get_rgb('#5271FF')
gray = get_rgb('#A6A6A6')

# Fonts
boldsans50 = loadFont("opensansbold.ttf", 50) 
boldsans35 = loadFont("opensansbold.ttf", 35) 
regularsans22 = loadFont("opensansregular.ttf", 22)

def MENU_MODE():

    title = boldsans50.render("Tic Tac Toe", False, black)
    title_rect = title.get_rect(center = (300,70))

    selected = True

    def button1Clicked():
        nonlocal selected
        selected = True

    def button2Clicked():
        nonlocal selected
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

    playBtn = Button(screen, (SCR_WIDTH - 200)//2, 400, 200, 70,
                    text="play",
                    font=boldsans35,
                    inactiveColour=blue,
                    hoverColour=gray,
                    pressedColour=gray,
                    textColour=white,
                    textHAlign='center',
                    textVAlign='center',
                    radius=100)

    playBtn.setOnClick(lambda: GAME_MODE(selected))
    
    # Fill white colour as background
    screen.fill(white)

    while True:
        events = pygame.event.get()

        for event in events:
            # QUIT event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()    

        button1.setInactiveColour(blue if selected else gray)
        button2.setInactiveColour(gray if selected else blue)
        screen.blit(title, title_rect)

        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick_busy_loop(60)

def GAME_MODE(game_type):
    '''
        Human vs Human: game_type is True
        Human vs Computer: game_type is False
    '''

    print(game_type)
    print("hello")

# Initial Start
MENU_MODE()