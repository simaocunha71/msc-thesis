def replace_char(string,old_char,new_char):
    """
    Replace characters in a string.

    Parameters:
        string (str): The string to be replaced.
        old_char (str): The character to be replaced.
        new_char (str): The character to replace with.

    Returns:
        str: The replaced string.
    """
    result = ""
    for char in string:
        if char == old_char:
            result += new_char
        else:
            result += char
    return result