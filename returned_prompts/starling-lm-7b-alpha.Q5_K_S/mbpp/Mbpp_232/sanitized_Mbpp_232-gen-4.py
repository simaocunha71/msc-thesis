def larg_nnum(lst, n):
    """
    Takes in a list and an integer n and returns a list containing the n largest items from the list.

    Parameters:
        lst (list): The list to be searched through.
        n (int): The number of largest items to return.

    Returns:
        list: The n largest items from the list.
    """
    # Sort the list in descending order
    lst.sort(reverse = True)
    # Return the first n items
    return lst[:n]