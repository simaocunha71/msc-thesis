def reverse_string_list(lst):
    """
    reverse_string_list(lst): This function will take a list of strings and reverse each string in the list.

    >>> reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])
    ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    """
    return [s[::-1] for s in lst]