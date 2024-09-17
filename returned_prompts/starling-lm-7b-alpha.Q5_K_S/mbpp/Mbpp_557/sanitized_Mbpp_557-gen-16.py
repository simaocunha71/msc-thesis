def toggle_string(str):
    """ Toggle the case of all characters in a string """
    return ''.join(c.lower() if c.isupper() else c.upper() for c in str)