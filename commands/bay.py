import re
import sys
sys.path.append("..")
import command_system
import random

def hello(id):
   message = ['пока', 'bay']
   num = random.randint(0, (len(message)-1))
   return message[num], ''

hello_command = command_system.Command()

hello_command.keys = ['пока', 'bay']
hello_command.description = 'Попращаюсь с тобой'
hello_command.process = hello