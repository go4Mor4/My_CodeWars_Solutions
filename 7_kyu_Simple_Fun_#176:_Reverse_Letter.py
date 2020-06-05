'''
Instructions

Loading description...
'''

#CODE
import re
def reverse_letter(string):
  string = re.sub('[^a-z]', '', string)
  return string[::-1]
