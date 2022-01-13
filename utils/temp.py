"""
This module have some
functions for work with the temperature
"""


# no use in the program
def convert_to_celcius(kelvin_value:float) -> float:
	"""
	Convet the kelvin value passed
	for parameter to celcius value, return
	the celcius value
	"""

	if type(kelvin_value) not in [float]:
		raise TypeError('The value for convert to celcius, not is a float value.')

	# getting
	result = kelvin_value - 273.15

	return result
