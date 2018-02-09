import re
import sys
sys.path.append("..")
import command_system
import vkApi
import random

def hello(id):
   first_name = vkApi.getStatus(id)
   print(first_name)
   message = ['Ну привет...', 'Привет', 'Здравствуй', 'Ку. Как дела?']
   num = random.randint(0, (len(message)-1))
   return message[num], ''

hello_command = command_system.Command()

hello_command.keys = ['hello', 'Ну привет...', 'Привет', 'Здравствуй', 'Ку']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello

