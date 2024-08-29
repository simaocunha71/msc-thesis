
def tuple_size(tup):
    return sys.getsizeof(tup)

print(tuple_size(("A", 1, "B", 2, "C", 3)))

# The above code will return the size in bytes of the tuple.
# sys.getsizeof() function returns the size of the object in bytes.

# Note: The size of the tuple calculated by sys.getsizeof() includes the space for the tuple itself, 
# along with the space for the references to the objects it contains. 
# Therefore, the size of the tuple might be larger than the sum of the sizes of the objects it contains.
<jupyter_output>
112
<jupyter_text>
Q2. Write a function that takes a list of numbers and returns a new list with distinct elements of the first list.
<jupyter_code>
def distinct_elements(lst):
    return list(set(lst))

print(distinct_elements([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]))
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7]
<jupyter_text>
Q3. Write a function to check if a given key already exists in a dictionary.
<jupyter_code>
def key_exists(d, key):
    return key in d

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(key_exists(d, 'a'))  # True
print(key_exists(d, 'e'))  # False
<jupyter_output>
True
False
<jupyter_text>
Q4. Write a function to merge two dictionaries.
<jupyter_code>
def merge_dicts(d1, d2):
    return {**d1, **d2}

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
