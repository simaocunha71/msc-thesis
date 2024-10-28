import re

def sort_numeric_strings(my_list):
    """
    Sorts a list of strings of numbers numerically
    """
    # convert each string to a float and sort numerically
    return sorted(my_list, key=lambda x: float(re.sub('[^0-9]', '', x)))

