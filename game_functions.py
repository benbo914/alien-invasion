import sys

import pygame

def check_events(ship):
    """Respond to keypresses and mouse clicks"""
    for event in pygame.event.get():
        # Quit game if window is closed
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    """Respond to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """Update images on the screen"""
    # Redraw screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make most recently drawn screen visible
    pygame.display.flip()
