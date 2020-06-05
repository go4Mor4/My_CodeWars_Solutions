'''
Instructions

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

#CODE
def pig_it(text):
    words, new_phrase = text.split(' '), ''
    for i in range(len(words)):
        if words[i] == '!' or words[i] == '?':
          new_phrase += words[i] + ' '
        else:
           new_phrase += words[i][1:] + words[i][0] + 'ay '
    return new_phrase[0:-1]
