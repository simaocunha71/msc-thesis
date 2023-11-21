

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    
    new_str = ''
    for letter in string:  # The "for" loop is the same way as a list comprehension of strings (or characters) from a given string.
        if letter == letter.lower():
            new_letter = letter.upper()
        else:
            new_letter = letter.lower()
        new_str += new_letter
    return new_str  # The return of the function is the same as the list comprehension, and that is converted to a string by calling the + operator with the given string value at the end.

if __name__ == '__main__':
    print(flip_case('Hello'))