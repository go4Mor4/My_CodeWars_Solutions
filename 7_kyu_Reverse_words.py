'''
Instructions

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

#CODE
def reverse_words(frase):
  palavras = frase.split(' ')
  palavras_reverso = []
  for palavra in palavras: palavras_reverso.append(palavra[::-1])
  return ' '.join(palavras_reverso)
