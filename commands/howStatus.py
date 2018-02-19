import sys
sys.path.append("..")
import command_system
import random
import vkApi

def hay(text):		
	try:
		if id == None:
			message = 'Введите id Пользователя.'
		else:	
			message = vkApi.getStatus(text)
	except Exception as e:
		message = str(e)
	finally:
		return message, ''
	
hello_command = command_system.Command()
hello_command.keys = ['статус']
hello_command.description = 'скажу статус'
hello_command.process = hay