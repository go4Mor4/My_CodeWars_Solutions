'''
Instructions

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''

#CODE
def solution(frase, final):
    final = final[::-1]
    frase = frase[::-1]
    for i in range(len(final)):
      if final[i] == frase[i] and len(final) <= len(frase):
        continue
      else:
        return False
        break
    return True
