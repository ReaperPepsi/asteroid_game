from circleshape import *
import pygame


class Shoot(CircleShape):
    def __init__(self, x, y, radius, direction: pygame.Vector2):
        super().__init__(x, y, radius)
        SHOT_SPEED = 500 # You can adjust this value!
        self.velocity = direction.normalize() * SHOT_SPEED

    def update(self, dt):
        # Update the position based on velocity and time elapsed (dt)
        # dt is typically a small number representing time in seconds since the last frame
        self.position[0] += self.velocity.x * dt
        self.position[1] += self.velocity.y * dt