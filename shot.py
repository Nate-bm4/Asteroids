from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "WHITE", self.position, self.radius, width = LINE_WIDTH)

    def update(self, dt):
         self.position += (self.velocity * dt)
