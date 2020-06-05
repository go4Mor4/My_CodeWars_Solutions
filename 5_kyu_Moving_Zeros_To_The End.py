'''
Instructions

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''
#CODE
def move_zeros(array):
  n_zeros = 0
  for i in range(len(array)):
      if array[i] is False: array[i] = 'False'
  for i in array:
      if i == 0: n_zeros += 1
  array = [value for value in array if value != 0]
  for i in range(n_zeros): array.append(0)
  for i in range(len(array)):
      if array[i] == 'False': array[i] = False
  return array
