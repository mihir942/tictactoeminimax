import pygame
from sys import exit

# Pygame Admin 
pygame.init()
pygame.display.set_caption("Tic Tac Toe")
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

# Fill white colour as background
white = (255,255,255)
screen.fill(white)

# Main Loop
while True:
    
    # loop to check for events
    for event in pygame.event.get():

        # QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()    
    
    pygame.display.update()
    clock.tick_busy_loop(60)
