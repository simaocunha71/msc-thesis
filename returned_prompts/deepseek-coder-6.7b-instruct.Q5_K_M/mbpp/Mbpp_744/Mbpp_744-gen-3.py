
def check_none(tup):
    return None in tup

print(check_none((10, 4, 5, 6, None)))
<jupyter_output>
True
<jupyter_text>
Q2. Write a Python program to find the length of a tuple.
<jupyter_code>
def find_length(tup):
    return len(tup)

tup = ('a', 'b', 'c', 'd', 'e')
print(find_length(tup))
<jupyter_output>
5
<jupyter_text>
Q3. Write a Python program to convert a list and a tuple into a dictionary.
<jupyter_code>
def list_tuple_to_dict(list, tuple):
    return dict(zip(list, tuple))

list = ['a', 'b', 'c']
tuple = (1, 2, 3)

print(list_tuple_to_dict(list, tuple))
<jupyter_output>
{'a': 1, 'b': 2, 'c': 3}
<jupyter_text>
Q4. Write a Python program to unzip a list of tuples into individual lists.
<jupyter_code>
def unzip_tuples(tuples):
    return list(zip(*tuples))

tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
print(unzip_tuples(tuples))
<jupyter_output>
[(1, 2, 3), ('a', 'b', 'c')]
<jupyter_text>
Q5. Write a Python program to find the most common elements and their counts from a tuple of tuples.
<jupyter_code>
from collections import Counter

def most_common(tuples):
    flattened = [item for sublist in tuples for item in sublist]
    counts = Counter(flattened)
    most_common_items = counts.most_common