import functools

def add_string(my_list, format_string):
    return [functools.reduce(lambda x,y: x+y, (format_string.format(x) for x in [i])) for i in my_list]

# A more concise way
def add_string(my_list, format_string):
    return [format_string.format(x) for x in my_list]

# A more concise way
def add_string(my_list, format_string):
    return [format_string % x for x in my_list]
