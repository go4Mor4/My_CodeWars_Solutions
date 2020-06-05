'''
Instructions

Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''

#CODE
def find_it(seq):
  for i in seq:
    c = seq.count(i)
    if c % 2 == 0: continue
    else: return i
