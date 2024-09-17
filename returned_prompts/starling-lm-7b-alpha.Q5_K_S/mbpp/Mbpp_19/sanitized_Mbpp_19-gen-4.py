def test_duplicate(array):
    """
    Input: array - a list of integers
    Output: True if there is any duplicate element in the list, False otherwise
    """
    array_set = set(array)
    if len(array)!=len(array_set):
        return True
    return False