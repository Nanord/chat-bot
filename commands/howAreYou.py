import re
import sys
sys.path.append("..")
import command_system
import random

def hello(id):
   message = ['Как дела?']
   num = random.randint(0, (len(message)-1))
   return message[num], ''

hello_command = command_system.Command()

hello_command.keys = ['как дела']
hello_command.description = 'Отвечу'
hello_command.process = hello


