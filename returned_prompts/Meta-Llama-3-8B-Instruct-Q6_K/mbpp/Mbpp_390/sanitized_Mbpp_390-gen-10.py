def add_string(lst, format_str):
    return [format_str.format(i) for i in lst]  # use list comprehension and str.format() method