import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while(True):

        # Check for player inputs
        # update the game world
        # draw the game to the screen

        #input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #game loop


        #draw
        screen.fill((1,1,1,1))
        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()


