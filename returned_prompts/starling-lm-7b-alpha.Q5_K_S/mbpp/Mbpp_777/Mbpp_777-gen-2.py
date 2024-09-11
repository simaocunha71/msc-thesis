def find_sum(lst):
    """
    Returns the sum of non-repeated elements in a given list.

    Parameters:
    lst (list): The list of integers.

    Returns:
    int: The sum of non-repeated elements in the list.
    """
    # Create a set from the list to remove any repeated elements
    s = set(lst)
    # Calculate the sum of the elements in the set
    return sum(s)


# Test the function
assert find_sum([1,2,3,1,1,4,5,6]) == 21

# Test with an empty list
assert find_sum([]) == 0

# Test with a list of only one element
assert find_sum([1]) == 1

# Test with a list of all the same elements
assert find_sum([1,1,1]) == 1

# Test with a list of negative integers
assert find_sum([-1,-2,-3]) == -6

# Test with a list of floating point numbers
assert find_sum([0.5, 0.2, 0.8]) == 1.5

# Test with a list of mixed data types
assert find_sum([1, 2, "3", 4, 5, 6]) == 15

# Test with a list of strings
assert find_sum(["1", "2", "3", "1", "1"]) == 6

# Test with a list of None values
assert find_sum([None, None, None]) == 0

# Test with a list of lists
assert find_sum([[1,2,3], [4,5,6], [1,1,1]]) == 15

# Test with a list of dictionaries
assert find_sum([{"a":1}, {"b":2}, {"c":3}, {"a":1}, {"a":1}]) == 6

# Test with a list of tuples
assert find_sum(((1,2,3), (4,5,6), (1,1,1))) == 15

# Test with a list of sets
assert find_sum({(1