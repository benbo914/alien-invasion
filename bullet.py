import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to handle bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create bullet object"""
        super(Bullet, self).__init__()
        self.screen = screen

        
