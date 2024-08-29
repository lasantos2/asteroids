import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    updatable_group.add(player)
    drawable_group.add(player)

    while(True):

        # Check for player inputs
        # update the game world
        # draw the game to the screen

        #input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updatable in updatable_group:
            updatable.update(dt)

        #game loop


        #draw
        
        screen.fill(pygame.Color(0,0,0))
        
        for drawable in drawable_group:
            drawable.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()


