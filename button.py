import pygame.font

class Button:
	def __init__(self, tg, msg):
		"""Initialize button attributes."""
		self.screen = tg.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = 227, 11, 93
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		

		# Build the button"s rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The button's message needs to be prepped only once.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color,
				self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Draw blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

class DifButtons(Button):
	"""Create different buttons for 3 different difficulties."""
	def __init__(self, tg, msg):
		"""Initialize button attributes."""
		super().__init__(tg, msg)
		self.button_color = 178, 147, 237
		self.width = 220
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.msg_image = self.font.render(msg, True, self.text_color,
				self.button_color)