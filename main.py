import pygame
from constants import *
from player import *
from asteroid import *
from shot import *
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group

    Player.containers = (updatable_group, drawable_group)
    Shot.containers = (shots_group, updatable_group, drawable_group)
    field = AsteroidField()

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updatable in updatable_group:
            updatable.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collision(player):
                print("Game Over!")
                exit()
 
        screen.fill("black")
        
        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()


