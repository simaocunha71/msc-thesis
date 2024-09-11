def count_first_elements(t):
    counter = 0
    for elem in t:
        if isinstance(elem, tuple):
            counter += 1
    return counter


assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3


def count_first_elements(t):
    counter = 0
    for elem in t:
        if isinstance(elem, tuple):
            counter += 1
    return counter


assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3



# Python program to find the
# number of elements in a tuple
# that occurs before the tuple element

def count_first_elements(t):
    counter = 0
    for elem in t:
        if isinstance(elem, tuple):
            counter += 1
    return counter

# Driver code
t = (1, 5, 7, (4, 6), 10)
print(count_first_elements(t))

# This code is contributed by PrinciRaj15
"""
The above code will return the number of tuples that occurs before the tuple element in the given tuple.
For example, if the given tuple is (1, 5, 7, (4, 6), 10), the function will return 3 because there are 3 tuples before the tuple (4, 6).
"""



# Python program to find the
# number of elements in a tuple
# that occurs before the tuple element

def count_first_elements(t):
    counter = 0
    for elem in t:
        if isinstance(elem, tuple):
            counter += 1
    return counter

# Driver code
t = (1, 5, 7, (4, 6), 10)
print(count_first_elements(t))

# This code is contributed by PrinciRaj15
"""
The above code will return the number of tuples that occurs before the tuple element in the given tuple.
For example, if the given tuple is (1, 5, 7, (4, 6