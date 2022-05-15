import pygame
from pygame.sprite import Sprite
from target_ship import Ship

class Bullet(Sprite):
	"""A bullet that will be shot from the ship."""

	def __init__(self, tg):
		"""Initialize starting attributes of the bullet."""
		self.settings = tg.settings
		self.screen = tg.screen
		self.ship = Ship(self)
		super().__init__()
		self.screen = tg.screen
		self.color = (247, 55, 24)

		# Set rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
				self.settings.bullet_height)
		
		self.rect.midright = tg.ship.rect.midright

		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal positon of the bullet.
		self.x += self.settings.bullet_speed
		
		# Update the rect position
		self.rect.x = self.x

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)