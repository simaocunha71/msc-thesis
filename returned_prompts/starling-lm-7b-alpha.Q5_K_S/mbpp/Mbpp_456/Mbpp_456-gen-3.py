def reverse_string_list(lst):
    return [s[::-1] for s in lst]

# Test
print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])) # ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']




"""
In this problem, we are given a list of strings, and we need to create a new list by reversing each string in the original list. 

To solve this problem, we can use a Python list comprehension to iterate over each string in the original list and use the slicing syntax `[::-1]` to reverse the characters in each string. 

The `[::-1]` slicing syntax means to start at the end of the string and end at position 0, moving with a step of -1 (i.e., one step backwards). This effectively reverses the order of the characters in the string. 

Finally, we return the new list of reversed strings. 

The provided test case demonstrates the usage of the `reverse_string_list` function with an example input list and prints the expected output. 
"""

# Here is a Python program that implements the solution:

def reverse_string_list(lst):
    return [s[::-1] for s in lst]

# Test
print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])) # ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

"""
The `reverse_string_list` function takes in a list of strings as its parameter. It uses a list comprehension to iterate over each string in the input list and applies the `[::-1]` slicing syntax to reverse the order of the characters in each string. The reversed strings are then collected into a new list, which is returned as the result. 

The provided test case demonstrates the usage of the `reverse_string_list` function with an example input list `['Red', 'Green', 'Blue', 'White', 'Black']` and prints the expected output `['deR', 'neerG', 'eulB', 'etihW