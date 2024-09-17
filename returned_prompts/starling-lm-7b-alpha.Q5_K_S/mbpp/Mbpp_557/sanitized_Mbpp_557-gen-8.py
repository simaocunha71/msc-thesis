def toggle_string(string):
    """
    >>> toggle_string("Python")
    "pYTHON"
    """
    # Toggle the case of all characters in a string
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result