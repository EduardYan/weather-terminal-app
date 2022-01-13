"""
This module have some functions for
work with the system.
"""


def clear_terminal() -> None:
	"""
	Clean the terminal validating
	the system for clear.
	"""

	from sys import platform
	from os import system

	# validating
	if platform == 'linux' or platform[:5] == 'linux':
		system('clear')

	elif platform == 'darwin':
		system('clear')

	elif platform == 'win32':
		system('cls')

	else:
		print(f'Other system found: {platform}')
