import pygame
from pygame.sprite import Sprite

class Rectangle(Sprite):
	"""A rectangle that moves up and down on the right side of the screeen."""
	def __init__(self, tg):
		super().__init__()
		self.settings = tg.settings
		self.screen = tg.screen
		self.screen_rect = self.screen.get_rect()

		# Dimensions and properties of the button.
		self.width, self.height = (15, 100)
		self.rectangle_color = (255, 87, 51)

		# Position of the rectangle
		self.rect = pygame.Rect(1150, 200, self.width, self.height)
		self.y = float(self.rect.y)

	def draw_rectangle(self):
		"""Draw rectangle to the screen."""
		pygame.draw.rect(self.screen, self.rectangle_color, self.rect)

	def check_edges(self):
		"""Return true if a rectangle hit the edge of the screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.top <= self.screen_rect.top or self.rect.bottom >= self.screen_rect.bottom:
			return True

	def update(self):
		"""Move the rectangle up and down."""
		self.y += (self.settings.rectangle_speed * 
				self.settings.rectangle_direction)
		self.rect.y = self.y