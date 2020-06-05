'''
Instructions

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

#CODE
def countBits(n):
    count = 0
    n_copia = 0
    v = 1
    while v < n:
        v = v * 2
    while n_copia != n:
      while v + n_copia <= n:
        n_copia += v
        count += 1
      v = v / 2
    return count
