def number_ctr(string):
    """
    Returns the number of digits in a given string
    """
    return sum(char.isdigit() for char in string)