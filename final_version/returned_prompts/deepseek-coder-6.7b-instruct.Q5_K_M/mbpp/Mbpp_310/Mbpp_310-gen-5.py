def string_to_tuple(string):
    return tuple(string)

print(string_to_tuple("python 3.0"))  # ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')

# OR

def string_to_tuple(string):
    return tuple(list(string))

print(string_to_tuple("python 3.0"))  # ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')

# OR

def string_to_tuple(string):
    return tuple(iter(string))

print(string_to_tuple("python 3.0"))  # ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')

# OR

def string_to_tuple(string):
    return tuple(map(str, string))

print(string_to_tuple("python 3.0"))  # ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')

# OR

def string_to_tuple(string):
    return tuple(iter(lambda s=iter(string): next(s)))

print(string_to_tuple("python 3.0"))  # ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')

# OR

def string_to_tuple(string):
    return tuple(iter(lambda s=iter(string), n=None: n if n is None else next(s)))

print(string_to_tuple("python 3.0"))  # ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')

# OR

def string_to_tuple(string):
    return tuple(iter(lambda s=iter(string), n=None: n if n is None else next(s)))

print(string_to_tuple("python 3