def tup_string(tup):
    return ''.join(tup)

# test the function
print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))  # prints "exercises"






# Another way to solve this problem:

def tup_string(tup):
    return ''.join(map(str, tup))

print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))  # prints "exercises"





# Another way to solve this problem:

def tup_string(tup):
    return ''.join(map(str, tup)).replace(' ', '')

print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))  # prints "exercises"





# Another way to solve this problem:

def tup_string(tup):
    return ''.join(map(str, tup)).replace(' ', '').replace(',', '')

print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))  # prints "exercises"





# Another way to solve this problem:

def tup_string(tup):
    return ''.join(map(str, tup)).replace(' ', '').replace(',', '').replace('\'', '')

print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))  # prints "exercises"





# Another way to solve this problem:

def tup_string(tup):
    return ''.join(map(str, tup)).replace(' ', '').replace(',', '').replace('\'', '').replace('"', '')

print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))  # prints "exercises"





# Another way to solve this problem:

def tup_string(tup):
    return ''.join(map(str, tup)).replace(' ', '').replace(',', '').replace('\'', '').replace('"', '').replace('{', '').replace('}', '')

print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))  # prints "exercises"





# Another way to solve this problem:

def tup_string(tup):
    return ''.join(map(str