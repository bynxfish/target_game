class GameStats:
	"""Track statistics for Target Practice."""

	def __init__(self, tg):
		"""Initialize statistics."""
		self.settings = tg.settings
		self.reset_stats()
		# Start Target Practice in an inactive state.
		self.game_active = False

		self.difficulty_active = True
			 
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.bullets_left = self.settings.bullet_limit