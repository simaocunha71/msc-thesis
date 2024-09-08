def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True

print(even_position([3,2,1])) # False
"""
This python function checks every even index of a list. If it finds a number at an even index that is not even, it returns False. If it goes through the entire list without finding any odd numbers at even indices, it returns True.
"""

# Exercise 2

