def add_string(lst, format_string):
    return [format_string.format(i) for i in lst]  # or use str.format() if available