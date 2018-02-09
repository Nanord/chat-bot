import os 
import importlib
import vkApi
from command_system import command_list
import sys

def damerau_levenshtein_distance(s1, s2):
   d = {}
   lenstr1 = len(s1)
   lenstr2 = len(s2)
   for i in range(-1, lenstr1 + 1):
       d[(i, -1)] = i + 1
   for j in range(-1, lenstr2 + 1):
       d[(-1, j)] = j + 1
   for i in range(lenstr1): 
       for j in range(lenstr2):
           if s1[i] == s2[j]:
               cost = 0
           else:
               cost = 1
           d[(i, j)] = min(
               d[(i - 1, j)] + 1,  # deletion
               d[(i, j - 1)] + 1,  # insertion
               d[(i - 1, j - 1)] + cost,  # substitution
           )
           if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
               d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
   return d[lenstr1 - 1, lenstr2 - 1]

def load_modules():
   files = os.listdir("commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])
   import info 

def get_answer(event):
  message, attachment = '', ''
  distance = len(event.text)
  command = None
  key = ''
  for c in command_list:
    for k in c.keys:
      d = damerau_levenshtein_distance(event.text, k)
      if d == 0 or d < distance * 0.4:
        if c.keys[0] == 'статус':
          message, attachment = c.process(event.text)
        else:
          message, attachment = c.process(event.user_id)
        return message, attachment      
      else:
        message = "Ничего не понятно, " + ". Напиши 'помощь', чтобы узнать мои команды"
        attachment = ''  
  return message, attachment

load_modules()
print('OK')