import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set starting position"""

        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship image
        self.image = pygame.image.load("xwing.gif")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)