import re
import sys
sys.path.append("..")
import command_system
import requests
import json


def weather():
	try:	
		session = requests.Session()
		response = session.get('http://api.openweathermap.org/data/2.5/weather?id=520555&appid=8755b322e242d5f1451906063a9dba33').json()
		humidity = str(response['main']['humidity'])
		speed = str(response['wind']['speed'])
		message = ('За окном: '
					+ response['weather'][0]['description']
					+ '\nТемпература'
		 			+ str(response['main']['temp'] - 273.15)
		 			+ '\nСкорость ветра: '
		 			+ speed + 'м/с'
		 			+ '\nВлажность: '
		 			+ humidity + '%')
		print(message)
		#req = requests.get('http://api.openweathermap.org/data/2.5/weather?id=520555&appid=8755b322e242d5f1451906063a9dba33')
		#req.json()
		#message = text
	except requests.exceptions.RequestException as e:
		print('weatherErr')
		message = str(e)
	return message, ''

weather_command = command_system.Command()

weather_command.keys = ['погода']
weather_command.description = 'Погода'
weather_command.process = weather