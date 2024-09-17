from functools import reduce
def add_string(list_str,format_str):
    return [format(format_str.format(i),'s') for i in list_str]