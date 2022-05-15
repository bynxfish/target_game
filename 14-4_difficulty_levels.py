import sys
from settings_2 import Settings
from time import sleep
import pygame
from rectangle import Rectangle
from target_ship import Ship
from bullet_2 import Bullet 
from button import Button
from button import DifButtons
from game_stats import GameStats

class TargetGame:
	"""A game where you shoot from a ship on the left at a moving rectangle 
	on the right.
	"""
	def __init__(self):
		"""Initialize starting attributes of the game."""
		pygame.init()
		self.settings = Settings()
		self.bg_color = (255, 179, 71)
		self.screen = pygame.display.set_mode(
			(1200, 800))
		self.screen_rect = self.screen.get_rect()
		
		self.bullets = pygame.sprite.Group()
		self.rectangles = pygame.sprite.Group()
		self.rectangle = Rectangle(self)
		self.ship = Ship(self)
		self.bullet = Bullet(self)
		self.stats = GameStats(self)
		self.buttons = []
		self._create_difficulty_buttons()
		# Make the play button
		self.play_button = Button(self, "play")
	
	def run_game(self):
		"""Define the main game loop."""
		while True:
			self._check_events()
			if self.stats.game_active == True and self.stats.difficulty_active == False: 
				self.ship.update()
				self._update_rectangle()
				self._check_events()
				self._update_bullets()

			self._update_screen()

	def _fire_bullet(self):
		"""Fire a bullet starting from the ship."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update bullet positions and get rid of old bullets."""
		self.bullets.update()
		# Get rid of bullets that have disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.right >= self.screen_rect.right:
				self._check_fired_bullets()
				self.bullets.remove(bullet)
		self._check_bullet_collisions()

	def _check_fired_bullets(self):
		"""Check if fired bullet hit edge of screen."""
		if self.stats.bullets_left > 1:
			# Decrement ships left.
			self.stats.bullets_left -= 1

			# Get rid of any remaing bullets.
			self.bullets.empty()

			# Center the ship.
			self.ship.center_ship()

			# Pause.
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _check_bullet_collisions(self):
		"""Respond to bullet collisions."""
		# Remove any bullet that has collided.
		collisions = pygame.sprite.groupcollide(
				self.bullets, self.rectangles, True, False)			
		if collisions:
			self.settings.increase_speed()

	def _check_events(self):
		"""Check keyboard and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
				self._check_difficulty_buttons(mouse_pos)

	def _create_difficulty_buttons(self):
		"""Create 3 buttons that change the difficulty of the game."""
		self.easy_button = DifButtons(self, "Sub Optimal")
		self.easy_button.rect.topleft = self.screen_rect.topleft
		self.easy_button.msg_image_rect.center = self.easy_button.rect.center
		self.buttons.append(self.easy_button)

		self.medium_button = DifButtons(self, "Average")
		self.medium_button.rect.midtop = self.screen_rect.midtop
		self.medium_button.msg_image_rect.center = self.medium_button.rect.center
		self.buttons.append(self.medium_button)

		self.hard_button = DifButtons(self, "Kinda Good")
		self.hard_button.rect.topright = self.screen_rect.topright
		self.hard_button.msg_image_rect.center = self.hard_button.rect.center
		self.buttons.append(self.hard_button)

	def _check_difficulty_buttons(self, mouse_pos):
		"""Assign the correct difficult to the game."""
		button_1 = self.easy_button.rect.collidepoint(mouse_pos)
		button_2 = self.medium_button.rect.collidepoint(mouse_pos)
		button_3 = self.hard_button.rect.collidepoint(mouse_pos)
		if button_1 and self.stats.difficulty_active:
			self.settings.easy = True
			self.stats.difficulty_active = False
		elif button_2 and self.stats.difficulty_active:
			self.settings.medium = True
			self.stats.difficulty_active = False
		elif button_3 and self.stats.difficulty_active:
			self.settings.hard = True
			self.stats.difficulty_active = False
		self.settings.start_difficulty()

	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks Play."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active and not self.stats.difficulty_active:
			# Reset the game settings
			self.settings.initialize_dynamic_settings()
			# Reset the game statistics.
			self.stats.reset_stats()
			self.stats.game_active = True

			# Get rid of any remaining bullets.
			self.bullets.empty()

			# Center the ship
			self.ship.center_ship()

			# Hid the mouse cursor
			pygame.mouse.set_visible(False)

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_q:
			sys.exit()
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
	
	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _update_rectangle(self):
		"""Check if the rectangle hits an edge and change it's direction."""
		self._check_rectangle_edges()
		self.rectangle.update()
	
	def _check_rectangle_edges(self):
		"""Check if the rectangle touched the edge of the screen."""
		if self.rectangle.check_edges():
			self._change_rectangle_direction()
			

	def _change_rectangle_direction(self):
		"""Change the direction of the rectangle."""
		self.settings.rectangle_direction *= -1

	def _update_screen(self):
		"""Update images on the screen, and flip to a new screen."""
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.rectangle.draw_rectangle()
		self.rectangles.add(self.rectangle)

		if self.stats.difficulty_active:
			for button in self.buttons:
				button.draw_button()

		# Draw the play button if the game is not active.
		if not self.stats.game_active:
			self.play_button.draw_button()
		
		pygame.display.flip()

if __name__ == '__main__':
	tg = TargetGame()
	tg.run_game()