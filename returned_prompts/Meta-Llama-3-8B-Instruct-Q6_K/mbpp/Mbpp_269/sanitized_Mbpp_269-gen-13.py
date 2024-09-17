def ascii_value(char):
    try:
        return ord(char)
    except TypeError:
        return "Error: Input must be a single character"