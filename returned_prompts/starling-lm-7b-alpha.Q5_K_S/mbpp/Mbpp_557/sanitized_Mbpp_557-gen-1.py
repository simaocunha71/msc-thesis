def toggle_string(string):
    """
    Toggle the case of all characters in a string.
    >>> toggle_string("Python") == "pYTHON"
    True
    >>> toggle_string("Hello, World!") == "hELLO, wORLD!"
    True
    """
    res = ""
    for char in string:
        if char == char.lower():
            res += char.upper()
        else:
            res += char.lower()
    return res