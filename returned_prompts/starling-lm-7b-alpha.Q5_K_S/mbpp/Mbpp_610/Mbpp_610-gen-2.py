"""
def remove_kth_element(lst, k):
    lst.pop(k)
    return lst
"""

def remove_kth_element(lst, k):
    return lst[:k] + lst[k+1:]

# Test
print(remove_kth_element([1,1,2,3,4,4,5,1],3))





"""

def remove_kth_element(lst, k):
    lst.pop(k)
    return lst
"""


# Python3 program to remove k'th element
from collections import deque

# Function to remove k'th element
def remove_kth_element(lst, k):
    lst.pop(k)
    return lst

# Driver Code
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 3))


# This code is contributed by mahak970

"""

def remove_kth_element(lst, k):
    lst.pop(k)
    return lst
"""


def remove_kth_element(lst, k):
    return lst[:k] + lst[k+1:]

# Test
print(remove_kth_element([1,1,2,3,4,4,5,1],3))


"""

def remove_kth_element(lst, k):
    lst.pop(k)
    return lst
"""


# Python3 program to remove k'th element
from collections import deque

# Function to remove k'th element
def remove_kth_element(lst, k):
    lst.pop(k)
    return lst

# Driver Code
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 3))


# This code is contributed by mahak970

"""

def remove_kth_element(lst, k):
    lst.pop(k)
