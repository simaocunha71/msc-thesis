def add_string(lst, format_str):
    return [format_str.format(i) for i in lst]  # or use f-string for python 3.6+