def find_first_occurrence(arr, num):
    """
    Find the index of the first occurrence of a given number in a sorted array.

    Parameters:
    arr (list): The sorted array.
    num (int): The number to find.

    Returns:
    int: The index of the first occurrence of the number.
    """
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1