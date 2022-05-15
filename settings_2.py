import pygame

class Settings:
	"""A class to store all settings for target game."""

	def __init__(self):
		"""Initaialize the game's static settings."""
		self.easy = False
		self.medium = False
		self.hard = False

		self.easy_difficulty = 1
		self.medium_difficulty = 2
		self.hard_difficulty = 20

		# Screen settings
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (255, 179, 71)
		
		# Bullet settings
		self.bullet_limit = 3
		self.bullet_width = 40
		self.bullet_height = 15
		self.bullets_allowed = 2

		# Ship speed
		self.ship_speed = 2
		
		# How quickly the game speeds up
		self.speedup_scale = 1.2
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.rectangle_speed = 0.2
		self.bullet_speed = 1.0
		self.rectangle_direction = -1

	def start_difficulty(self):
		"""Choose the difficult to start the game."""
		if self.easy:
			self.bullet_width = 60
			self.bullet_height = 40
			self.rectangle_speed *= self.easy_difficulty
			self.bullet_speed *= self.easy_difficulty
		elif self.medium:
			self.rectangle_speed *= self.medium_difficulty
			self.bullet_speed *= self.medium_difficulty
		elif self.hard:
			self.bullet_width = 20
			self.bullet_height = 8
			self.rectangle_speed *= self.hard_difficulty
			self.bullet_speed *= self.hard_difficulty

	
	def increase_speed(self):
		"""Initialize speed settings."""
		self.rectangle_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		