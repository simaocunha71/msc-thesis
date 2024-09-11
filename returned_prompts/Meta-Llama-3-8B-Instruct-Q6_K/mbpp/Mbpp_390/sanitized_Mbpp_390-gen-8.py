def add_string(lst, fmt):
    return [fmt.format(i) for i in lst]  # Python 3.x
    # return [fmt % i for i in lst]  # Python 2.x