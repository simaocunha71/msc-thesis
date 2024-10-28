def issort_list(lst):
    """
    Function to check whether a specified list is sorted or not
    Parameters:
        lst: list
    Returns:
        True if the list is sorted, False otherwise
    """
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True