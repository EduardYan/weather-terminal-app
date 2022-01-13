"""
This module have the mode
for the city
"""

class City:
	"""
	Create a city with this properties:
	name
	temp
	description
	icon
	temp
	temp_max
	temp_min

	"""

	def __init__(
		self,
		name:str,
		country:str,
		description:str,
		# icon:str,
		temp:float,
		temp_max:float,
		temp_min:float
	):

		# values
		self.name = name
		self.country = country
		self.description = description
		# self.icon = icon # this was a test i will not ocuppy it
		self.temp = temp
		self.temp_max = temp_max
		self.temp_min = temp_min
