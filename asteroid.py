from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen,
                           pygame.Color(255,255,255),
                           center=self.position,
                           radius=self.radius,
                           width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        
        vector_asteroid_1 = self.velocity.rotate(random_angle)
        vector_asteroid_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)

        ast1.velocity = vector_asteroid_1 * 1.2
        ast2.velocity = vector_asteroid_2 * 1.2

        