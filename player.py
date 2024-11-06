import os
import pygame as pg

# Create a Player class that is a subclass of pygame.sprite.Sprite
# Load an image as such:
#        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
# The position is controlled by the rectangle surrounding the image.
# Set self.rect = self.image.get_rect().  Then make changes to the 
# rectangle x, y or centerx and centery to move the object.

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # Load the player's spaceship image
        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
        # Set up the rectangle for positioning
        self.rect = self.image.get_rect()
        # Initialize the starting position
        self.rect.center = start_pos
        # Define the player's speed
        self.speed = 300  # Pixels per second

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def up(self, delta):
        
        self.rect.y -= self.speed * delta
       
        if self.rect.top < 0:
            self.rect.top = 0
        pass

    def down(self, delta):
        self.rect.y += self.speed * delta

        if self.rect.bottom > 768:
            self.rect.bottom = 768
        pass
