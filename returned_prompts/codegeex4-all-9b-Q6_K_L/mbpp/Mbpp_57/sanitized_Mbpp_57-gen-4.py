def find_Max_Num(digits):
    """
    Finds the largest number that can be formed with the given list of digits.
    :param digits: List of digits
    :return: Largest number formed
    """
    # Convert the list of digits to a string
    digits_str = ''.join(str(digit) for digit in digits)
    
    # Convert the string to a list and sort it in descending order
    sorted_digits = sorted(digits_str, reverse=True)
    
    # Convert the sorted list back to a string and then to an integer
    largest_number = int(''.join(sorted_digits))
    
    return largest_number