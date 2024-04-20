"""
Write a python function which takes a list of integers and only returns the odd ones.
assert Split([1,2,3,4,5,6]) == [1,3,5]
"""
def split(numbers):
    return [n for n in numbers if (mod(num, 2) != 0)]
  
def mod(x, y):
    return x % y