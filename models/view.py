"""
This module have the class
for have a mode of a view
in the terminal

"""

from requests import get
from data.cities import CITIES
from config import APPID
from models.city import City
from data.colors import GREEN, BLUE, PURPLE

class View:
	""""
	Model for the view.
	"""

	def get_data(self, city_name) -> dict:
		"""
		Return a dict, of the request
		to restapi
		"""

		request = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=en&units=metric&appid={APPID}'

		try:
			response = get(request)
	
			data = response.json()

			return data

		except ConnectionError:
			# in case this error
			print('\nConnection Error')

	def show_info(self) -> None:
		"""
		Show in the terminal
		the weather of the citees
		With the colors of colorama
		"""

		print()

		for city in CITIES:
			data = self.get_data(city)

			# getting the data of each city
			name_city = data['name']

			country_city = data['sys']['country']

			description_city = data['weather'][0]['description']

			temp_city = data['main']['temp']
			temp_max_city = data['main']['temp_max']

			temp_min_city = data['main']['temp_min']

			# model for the city
			city = City(
				name_city,
				country_city,
				description_city,
				temp_city,
				temp_max_city,
				temp_min_city

			)



			# showing data
			print(GREEN + f'{city.name} => {city.country}')
			print(f'Status (English) {city.description}')

			print(f'Current Temperature {BLUE + str(city.temp)} celsius')

			print(f'Maximum Temperature {BLUE + str(city.temp_max)} celsius')

			print(f'Minimum Temperature {BLUE + str(city.temp_min)} celsius')


			print(PURPLE + '-----------------------------')
			print()
