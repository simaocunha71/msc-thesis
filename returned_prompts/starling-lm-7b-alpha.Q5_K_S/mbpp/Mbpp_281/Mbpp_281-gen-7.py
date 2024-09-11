def all_unique(lst):
    """
    This function will return True if all the elements of a given list are unique and False otherwise

    Parameters:
    lst(list): The list of integers

    Returns:
    bool: True if all the elements of the list are unique, False if not
    """
    seen = set()
    for elem in lst:
        if elem in seen:
            return False
        seen.add(elem)
    return True

# Test
assert all_unique([1,2,3]) == True
assert all_unique([1,1,2,3]) == False


# Other Solution
def all_unique(lst):
    """
    This function will return True if all the elements of a given list are unique and False otherwise

    Parameters:
    lst(list): The list of integers

    Returns:
    bool: True if all the elements of the list are unique, False if not
    """
    return len(lst) == len(set(lst))

# Test
assert all_unique([1,2,3]) == True
assert all_unique([1,1,2,3]) == False







































"""
Explanation:
The function all_unique takes a list as an argument and checks if all the elements in the list are unique. It does this by creating a set called seen, which will store the elements of the list as they are encountered. Then, it iterates over the list and checks if each element is already in the set. If an element is already in the set, it means it has been encountered before, so the function returns False. If all the elements are unique, the function returns True.

The second solution uses the built-in set function to create a set of unique elements from the list. It then compares the length of the list to the length of the set. If the lengths are equal, it means all the elements in the list are unique, so the function returns True. Otherwise, it returns False.
"""






















