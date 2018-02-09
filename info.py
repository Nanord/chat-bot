import sys
sys.path.append("..")
import command_system

def info(id):
   message = ''
   for c in command_system.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
   return message, ''

info_command = command_system.Command()

info_command.keys = ['help', 'help me']
info_command.desciption = 'Расскажу команды'
info_command.process = info