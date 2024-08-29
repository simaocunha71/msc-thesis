
def get_equal(lst):
    for tup in lst:
        if len(tup) != len(lst[0]):
            return False
    return True

print(get_equal([(11, 22, 33), (44, 55, 66)]))  # True

"""
The function get_equal takes a list of tuples as an argument.
Then it loops through the list of tuples and checks whether the length of each tuple is equal to the length of the first tuple in the list. If it finds a tuple with a length not equal to the first tuple's length, it returns False. If it goes through all tuples without finding one with a length not equal to the first, it returns True.
"""

# Solution 2:
def get_equal(lst):
    return all(len(tup) == len(lst[0]) for tup in lst)

print(get_equal([(11, 22, 33), (44, 55, 66)]))  # True

"""
The function get_equal uses the built-in function all. This function returns True if all elements in an iterable are true.
It checks whether the length of each tuple in the list is equal to the length of the first tuple. If all tuples have the same length, all will return True. If not, all will return False.
"""
<jupyter_output>
True
True
<jupyter_text>
Problem 4
<jupyter_code>
