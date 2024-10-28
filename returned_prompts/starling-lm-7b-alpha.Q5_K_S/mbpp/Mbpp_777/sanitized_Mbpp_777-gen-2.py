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