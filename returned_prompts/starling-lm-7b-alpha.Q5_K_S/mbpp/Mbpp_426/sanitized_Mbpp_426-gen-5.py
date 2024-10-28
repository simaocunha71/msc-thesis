def filter_oddnumbers(num_list):
    """
    Filter odd numbers from a given list of numbers

    Parameters
    ----------
    num_list : list
        List of numbers

    Returns
    -------
    list
        List with only odd numbers
    """
    odd_numbers = []
    for num in num_list:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers