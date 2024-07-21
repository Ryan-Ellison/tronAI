import pygame
from pygame.locals import *
from vector import Vector2
from constants import *

class TronPlayer(object):
    def __init__(self):
        self.name = TRONPLAYER
        self.position = Vector2(200, 400)
        self.directions = {STOP: Vector2(), UP: Vector2(0, -1), DOWN: Vector2(0, 1), LEFT: Vector2(-1, 0), RIGHT: Vector2(1, 0)}
        self.direction = STOP
        self.speed = 100 * TILEWIDTH / 16
        self.radius = 10
        self.color = BLUE

    def update(self, dt):
        self.position += self.directions[self.direction] * self.speed * dt
        direction = self.getValidKey()
        self.direction = direction

    def getValidKey(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[K_UP]:
            return UP
        if keyPressed[K_DOWN]:
            return DOWN
        if keyPressed[K_LEFT]:
            return LEFT
        if keyPressed[K_RIGHT]:
            return RIGHT
        
        return self.direction
    
    def render(self, screen):
        pos = self.position.asIntTuple()
        pygame.draw.circle(screen, self.color, pos, self.radius)