
class Settings():
    """A class to store all settings for the game"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 780
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 5

        # Bullet Settings
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0 
