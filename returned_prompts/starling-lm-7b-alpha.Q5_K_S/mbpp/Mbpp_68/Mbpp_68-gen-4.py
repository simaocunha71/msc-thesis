"""
def is_monotonic(list):
    # Check if the list is sorted in ascending order
    if list == sorted(list):
        return True
    # Check if the list is sorted in descending order
    elif list == sorted(list, reverse=True):
        return True
    # If the list is neither sorted in ascending or descending order, the list is not monotonic
    else:
        return False

list = [6, 5, 4, 4]
print(is_monotonic(list)) # True
"""

# In order to check whether the given array is monotonic or not, we can use the sorted() function in Python. The sorted() function returns a new list with all elements sorted in ascending order by default. If the original list is sorted in ascending order, the sorted() function will return the same list. If the original list is sorted in descending order, the sorted() function will return a new list with the elements sorted in ascending order. If the original list is neither sorted in ascending or descending order, the sorted() function will return a new list with the elements sorted in ascending order. By comparing the returned list with the original list, we can determine whether the given array is monotonic or not.

# In the provided code, the function is_monotonic takes a list as input and checks whether the list is monotonic or not. It first checks if the list is sorted in ascending order using the sorted() function. If the returned list is the same as the original list, the function returns True, indicating that the list is monotonic. If the returned list is not the same as the original list, the function checks if the list is sorted in descending order using the sorted() function with the reverse parameter set to True. If the returned list is the same as the original list, the function returns True, indicating that the list is monotonic. If the returned list is not the same as the original list, the function returns False, indicating that the list is not monotonic.

# The provided code includes an example of how to use the is_monotonic function. It creates a list [6, 5, 4, 4] and passes it to the is_monotonic function. The function returns True, indicating that the list [6