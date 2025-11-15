from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        return pygame.draw.circle(screen, "WHITE", self.position, self.radius, width = LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            positive_angle = self.velocity.rotate(angle)
            negative_angle = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one, asteroid_two = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_one.velocity = positive_angle * 1.2
            asteroid_two.velocity = negative_angle * 1.2
