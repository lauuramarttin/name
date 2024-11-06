import os
import pygame as pg

# Create an Enemy class that is a subclass of pygame.sprite.Sprite
class Enemy(pg.sprite.Sprite):
    def __init__(self, start_pos=(512, -50), speed=100):
        super(Enemy, self).__init__()
        # Load the enemy image
        self.image = pg.image.load(os.path.join('assets', 'Enemy.png')).convert_alpha()
        # Set up the rectangle for positioning
        self.rect = self.image.get_rect()
        # Initialize the starting position
        self.rect.center = start_pos
        # Define the enemy's speed
        self.speed = speed  # Pixels per second

    def update(self, delta):
        # Move the enemy down by increasing the y-coordinate
        self.rect.y += self.speed * delta
        # Check if the enemy is off the screen (bottom) and reset if necessary
        if self.rect.top > 768:  # Assuming screen height of 768
            self.rect.bottom = 0  # Reset position to the top of the screen

    def draw(self, screen):
        # Draw the enemy on the given screen
        screen.blit(self.image, self.rect)

