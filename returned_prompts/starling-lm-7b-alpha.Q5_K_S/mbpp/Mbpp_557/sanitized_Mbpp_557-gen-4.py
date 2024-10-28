def toggle_string(string):
    result = ""
    for c in string:
        if c.isupper():
            result += c.lower()
        else:
            result += c.upper()
    return result