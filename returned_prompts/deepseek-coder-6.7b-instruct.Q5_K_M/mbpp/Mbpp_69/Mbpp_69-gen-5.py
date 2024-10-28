
def is_sublist(g, s):
  return all(i in g for i in s)
"""
The function is_sublist checks if all elements in the sublist 's' are in the main list 'g'. The built-in function 'all' returns True if all elements in the iterable (in this case the generator expression) are true.
"""

