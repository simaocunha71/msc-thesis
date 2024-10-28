
def and_tuples(tup1, tup2):
  return tuple(a & b for a, b in zip(tup1, tup2))
"""
This function works by using the built-in zip function to pair up the elements from the two tuples, and then it uses a generator expression to create a new tuple which consists of the bitwise and of the pair of elements.
"""

