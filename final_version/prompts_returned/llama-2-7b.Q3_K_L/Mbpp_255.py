"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""
from itertools import product
def combinations_colors( colors, n):
   """Combinations of colors"""
   return list( product( colours, repeat=n ))