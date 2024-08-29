def index_minimum(lst):
    lst.sort(key = lambda x: x[1])
    return lst[0][0]

print(index_minimum([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))

"""
The function index_minimum takes a list of tuples as an argument. It sorts the list of tuples based on the second element of each tuple, and then returns the first element of the first tuple in the sorted list (i.e., the tuple with the smallest second element).
"""

# Q2:
"""
Write a Python program to sort a tuple by its float element.
Sample Tuple: [('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]
Expected Output: [('Varsha', 100), ('Rash', 143), ('Manjeet', 200)]
"""

A2:
def sort_tuple(lst):
    return sorted(lst, key = lambda x: x[1])

print(sort_tuple([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))

"""
The function sort_tuple takes a list of tuples as an argument. It sorts the list of tuples based on the second element of each tuple (i.e., the float element) and returns the sorted list.
"""

# Q3:
"""
Write a Python program to combine values in python list of dictionaries.

Sample Data :
[{'item': 'item1', 'amount': 300}, {'item': 'item2', 'amount': 200}, {'item': 'item1', 'amount': 100}]

Expected Output:
[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 200}]
"""

A3:
from collections import defaultdict

def combine_values(lst):
    d = defaultdict(int)
    for dic in lst: