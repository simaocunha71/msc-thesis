
def add_tuple(lst, tup):
    return lst + list(tup)

print(add_tuple([5, 6, 7], (9, 10)))  # [5, 6, 7, 9, 10]

# Alternative solution:

def add_tuple(lst, tup):
    lst.extend(tup)
    return lst

print(add_tuple([5, 6, 7], (9, 10)))  # [5, 6, 7, 9, 10]

# Alternative solution:

def add_tuple(lst, tup):
    for item in tup:
        lst.append(item)
    return lst

print(add_tuple([5, 6, 7], (9, 10)))  # [5, 6, 7, 9, 10]

"""
Write a function that takes a list of words and returns a dictionary where the key is the word and the value is the length of the word.
assert get_lengths(["hello", "world"]) == {"hello": 5, "world": 5}
"""

