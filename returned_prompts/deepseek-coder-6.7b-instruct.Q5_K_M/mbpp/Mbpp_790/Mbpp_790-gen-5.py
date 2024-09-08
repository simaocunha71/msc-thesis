
def even_position(lst):
    return all(el % 2 == 0 for i, el in enumerate(lst) if i % 2 == 0)

print(even_position([3,2,1])) # False
"""
In the above function, we are iterating over the elements in the list with their indices. We only consider the elements at even indices (those where the index is even). We check if the number at the even index is even. If it isn't, the function returns False. If all numbers at even indices are even, the function returns True.
"""

# Another approach could be using list slicing, which is more pythonic and efficient.
def even_position(lst):
    return all(el % 2 == 0 for el in lst[::2])

print(even_position([3,2,1])) # False
"""
This function does the same thing as the previous one, but it uses list slicing to only consider the elements at even indices.
"""

# Another approach could be using for loop.
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True

print(even_position([3,2,1])) # False
"""
This function also iterates over the elements in the list, but it only considers the elements at even indices. It checks if the number at the even index is even. If it isn't, the function returns False. If all numbers at even indices are even, the function returns True.
"""

# Another approach could be using a while loop.
def even_position(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            return False
        i += 2
    return True

print(even_position([3,2,1])) # False
"""
This function also iterates over the elements in the list, but it only considers the elements at even indices. It checks if the number at the even index is even. If it isn't, the function returns False. If all numbers at even indices are even, the function returns True.
"""