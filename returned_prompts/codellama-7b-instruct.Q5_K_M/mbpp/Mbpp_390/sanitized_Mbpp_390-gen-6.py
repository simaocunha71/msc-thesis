import string
def add_string(list, format_string):
    return [format_string.format(i) for i in list]