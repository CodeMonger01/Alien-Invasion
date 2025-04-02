import math
from math import trunc


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_speed = 15
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 30
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20

        # Alien settings
        self.fleet_drop_speed = 5

        # How quickly the game speeds up
        self.speedup_scale = 1.35

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed = 5
        self.alien_speed = 2

        # fleet_direction of 1 represent right, -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = math.ceil(self.alien_points * self.score_scale)
        print(self.alien_points)
