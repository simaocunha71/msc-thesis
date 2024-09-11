def add_string(lst, fmt_str):
    return [fmt_str.format(i) for i in lst]  # or use list comprehension
    # return [fmt_str.format(i) for i in lst] if you want to use a list comprehension