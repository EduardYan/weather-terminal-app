""""
This is the principal file
for execute the weather app


Cancel the program with CTRL + C

"""

from models.view import View
from colorama import init
from utils.system import clear_terminal
from messages.info import INFO_MESSAGE
from data.colors import YELLOW


if __name__ == '__main__':
	view = View()

	# loop
	while True:
		try:
			print(YELLOW + INFO_MESSAGE)
			init(autoreset = True) # for not repeat the colors
			view.show_info()
			clear_terminal()

		except KeyboardInterrupt:
			# for ctrl + c
			break

	print()
